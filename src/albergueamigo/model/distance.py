'''
Created on 09/12/2010

@author: caio
'''

import math

# ----------------------------------------------------------------------
# | Algrothims from Geocentric Datum of Australia Technical Manual      |
# |                                                                     |
# | http://www.anzlic.org.au/icsm/gdatum/chapter4.html                  |
# |                                                                     |
# | This page last updated 11 May 1999                                  |
# |                                                                     |
# | Computations on the Ellipsoid                                       |
# |                                                                     |
# | There are a number of formulae that are available                   |
# | to calculate accurate geodetic positions,                           |
# | azimuths and distances on the ellipsoid.                            |
# |                                                                     |
# | Vincenty's formulae (Vincenty, 1975) may be used                    |
# | for lines ranging from a few cm to nearly 20,000 km,                |
# | with millimetre accuracy.                                           |
# | The formulae have been extensively tested                           |
# | for the Australian region, by comparison with results               |
# | from other formulae (Rainsford, 1955 & Sodano, 1965).               |
# |                                                                     |
# | * Inverse problem: azimuth and distance from known                  |
# |                     latitudes and longitudes                        |
# | * Direct problem: Latitude and longitude from known                 |
# |                     position, azimuth and distance.                 |
# | * Sample data                                                       |
# | * Excel spreadsheet                                                 |
# |                                                                     |
# | Vincenty's Inverse formulae                                         |
# | Given: latitude and longitude of two points                         |
# |                     (phi1, lembda1 and phi2, lembda2),              |
# | Calculate: the ellipsoidal distance (s) and                         |
# | forward and reverse azimuths between the points (alpha12, alpha21). |
# |                                                                     |
# ---------------------------------------------------------------------- 

def vinc_dist(phi1,  lembda1,  phi2,  lembda2 ) :
        """ 

        Returns the distance between two geographic points on the ellipsoid
        and the forward and reverse azimuths between these points.
        lats, longs and azimuths are in radians, distance in metres 

        Returns ( s, alpha12,  alpha21 ) as a tuple

        """
        phi1 = math.radians(phi1)
        phi2 = math.radians(phi2)
        
        lembda1 = math.radians(lembda1)
        lembda2 = math.radians(lembda2)
        
        a = 6378137
        f = 1/298.257223563
        if (abs( phi2 - phi1 ) < 1e-8) and ( abs( lembda2 - lembda1) < 1e-8 ) :
            return 0.0, 0.0, 0.0
  
        two_pi = 2.0*math.pi

        b = 6356752.314245

        TanU1 = (1-f) * math.tan( phi1 )
        TanU2 = (1-f) * math.tan( phi2 )
        
        U1 = math.atan(TanU1)
        U2 = math.atan(TanU2)

        lembda = lembda2 - lembda1
        last_lembda = -4000000.0                # an impossibe value
        omega = lembda

        # Iterate the following equations, 
        #  until there is no significant change in lembda 
        
        while ( last_lembda < -3000000.0 or lembda != 0 and abs( (last_lembda - lembda)/lembda) > 1.0e-9 ) :
        
          sqr_sin_sigma = pow( math.cos(U2) * math.sin(lembda), 2) + \
                pow( (math.cos(U1) * math.sin(U2) - \
                math.sin(U1) *  math.cos(U2) * math.cos(lembda) ), 2 )

          Sin_sigma = math.sqrt( sqr_sin_sigma )
          
          Cos_sigma = math.sin(U1) * math.sin(U2) + math.cos(U1) * math.cos(U2) * math.cos(lembda)
          
          sigma = math.atan2( Sin_sigma, Cos_sigma )

          Sin_alpha = math.cos(U1) * math.cos(U2) * math.sin(lembda) / math.sin(sigma)
          alpha = math.asin( Sin_alpha )
          
          Cos2sigma_m = math.cos(sigma) - (2 * math.sin(U1) * math.sin(U2) / pow(math.cos(alpha), 2) )
          
          C = (f/16) * pow(math.cos(alpha), 2) * (4 + f * (4 - 3 * pow(math.cos(alpha), 2)))
          
          last_lembda = lembda
          
          lembda = omega + (1-C) * f * math.sin(alpha) * (sigma + C * math.sin(sigma) * \
                (Cos2sigma_m + C * math.cos(sigma) * (-1 + 2 * pow(Cos2sigma_m, 2) )))
        

        u2 = pow(math.cos(alpha),2) * (a*a-b*b) / (b*b)
        
        A = 1 + (u2/16384) * (4096 + u2 * (-768 + u2 * (320 - 175 * u2)))
        
        B = (u2/1024) * (256 + u2 * (-128+ u2 * (74 - 47 * u2)))
        
        delta_sigma = B * Sin_sigma * (Cos2sigma_m + (B/4) * \
                (Cos_sigma * (-1 + 2 * pow(Cos2sigma_m, 2) ) - \
                (B/6) * Cos2sigma_m * (-3 + 4 * sqr_sin_sigma) * \
                (-3 + 4 * pow(Cos2sigma_m,2 ) )))
        
        s = b * A * (sigma - delta_sigma)
        
        alpha12 = math.atan2( (math.cos(U2) * math.sin(lembda)), \
                (math.cos(U1) * math.sin(U2) - math.sin(U1) * math.cos(U2) * math.cos(lembda)))
        
        alpha21 = math.atan2( (math.cos(U1) * math.sin(lembda)), \
                (-math.sin(U1) * math.cos(U2) + math.cos(U1) * math.sin(U2) * math.cos(lembda)))

        if ( alpha12 < 0.0 ) : 
                alpha12 =  alpha12 + two_pi
        if ( alpha12 > two_pi ) : 
                alpha12 = alpha12 - two_pi

        alpha21 = alpha21 + two_pi / 2.0
        if ( alpha21 < 0.0 ) : 
                alpha21 = alpha21 + two_pi
        if ( alpha21 > two_pi ) : 
                alpha21 = alpha21 - two_pi

        return s
