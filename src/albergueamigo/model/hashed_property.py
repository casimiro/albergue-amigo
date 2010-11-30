import hashlib, random

def salted_hexdigest(hash_constructor):
    """Convert a hashlib function to a function that can be used as hash
    function for a string value and a salt."""
    def hashfunc(value, salt):
        return hash_constructor(value + salt).hexdigest()
    return hashfunc

sha1_hash = salted_hexdigest(hashlib.sha1)

hex_chars = "0123456789abcdef"

def random_string(length, chars=hex_chars):
    """Creates a random string generating function.
    
    length
        Length of the strings to generate
    
    chars
        Sequence of characters to use. Defaults to hex characters.
    """
    def salt():
        return ''.join(random.choice(chars) for i in xrange(length))
    return salt

class _HashComparator(object):
    """A comparator for comparing strings against a hashed value."""
    def __init__(self, hashfunc, hash, salt):
        self.hashfunc = hashfunc
        self.hash = hash
        self.salt = salt
        
    def __eq__(self, other):
        return self.hash == self.hashfunc(other, self.salt)

    def __ne__(self, other):
        return self.hash != self.hashfunc(other, self.salt)

class HashedProperty(object):
    """A property that stores string values as a hash and a salt and can be
    compared for equality."""
    def __init__(self, hash_column, salt_column, hashfunc=sha1_hash,
                       saltfunc=random_string(40), dbhashfunc=None):
        """Create a property that stores string values as a hash and a salt
        and can be compared for equality.
        
        hash_column
            The attribute name the hashed value is stored in.
            
        salt_column
            The attribute name the salt value is stored in.
            
        hashfunc
            The function that is used to hash the value and the salt. Takes as
            parameters the value and the salt.
            
            Defaults to taking the SHA1 hexdigest of the concatenation of the
            value and the salt.
            
        saltfunc
            The function that is used to generate the salt value.
            
            Defaults to a 40 character random hex string.
        
        dbhashfunc
            The function that generates an equivalent hash on the database.
        """
        self.hash_column = hash_column
        self.salt_column = salt_column
        self.hashfunc = hashfunc
        self.dbhashfunc = dbhashfunc
        self.saltfunc = saltfunc

    def __get__(self, instance, owner):
        if instance is None:
            if self.dbhashfunc is None:
                raise NotImplementedError("Cannot query the database based on the hash func")
            hashfunc, parent = self.dbhashfunc, owner
        else:
            hashfunc, parent = self.hashfunc, instance
        return _HashComparator(hashfunc, getattr(parent, self.hash_column), getattr(parent, self.salt_column))

    def __set__(self, instance, value):
        salt = self.saltfunc()
        setattr(instance, self.salt_column, salt)
        setattr(instance, self.hash_column, self.hashfunc(value, salt))
