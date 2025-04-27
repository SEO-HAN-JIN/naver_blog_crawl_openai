package com.biz.nbcp.domain.user;

import lombok.Getter;

@Getter
public enum RoleEnum {
    ADMIN("관리자"),
    USER("사용자");

    private final String description;

    RoleEnum(String description) {
        this.description = description;
    }

}
