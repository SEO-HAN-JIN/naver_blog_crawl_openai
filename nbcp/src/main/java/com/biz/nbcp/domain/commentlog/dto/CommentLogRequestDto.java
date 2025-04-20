package com.biz.nbcp.domain.commentlog.dto;

import lombok.Getter;
import lombok.Setter;

@Getter
@Setter
public class CommentLogRequestDto {

    private Long id;
    private String userId;
    private String blogUrl;
    private String comment;
}
