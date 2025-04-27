package com.biz.nbcp.security.jwt;

public final class JwtProperties {
    public static final String SECRET_KEY = System.getProperty("jwt.secret_key");
    public static final int EXPIRATION_TIME = 1000 * 60 * 60 * 24 * 7; // 일주일
    public static final String TOKEN_PREFIX = "Bearer ";
    public static final String HEADER = "Authorization";
}
