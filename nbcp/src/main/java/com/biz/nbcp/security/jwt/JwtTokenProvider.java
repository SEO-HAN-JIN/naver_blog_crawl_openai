package com.biz.nbcp.security.jwt;


import com.auth0.jwt.JWT;
import com.auth0.jwt.algorithms.Algorithm;
import org.springframework.security.core.Authentication;
import org.springframework.stereotype.Component;

import java.util.Date;

@Component
public class JwtTokenProvider {

    public String generateToken(Authentication authentication) {
        String userId = authentication.getPrincipal().toString();

        String jwtToken = JWT.create()
                .withSubject("nbcp")
                .withExpiresAt(new Date(System.currentTimeMillis() + JwtProperties.EXPIRATION_TIME))
                .withClaim("userId", userId)
                .sign(Algorithm.HMAC512(JwtProperties.SECRET_KEY.getBytes()));

        return JwtProperties.TOKEN_PREFIX + jwtToken;
    }
}
