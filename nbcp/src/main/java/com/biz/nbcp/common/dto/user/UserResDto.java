package com.biz.nbcp.common.dto.user;

import com.biz.nbcp.domain.user.User;
import lombok.Data;

@Data
public class UserResDto {

    private String userId;
    private String password;
    private String role;

    public UserResDto(User user) {
        this.userId = user.getUserId();
        this.password = user.getPassword();
        this.role = user.getRole();
    }
}
