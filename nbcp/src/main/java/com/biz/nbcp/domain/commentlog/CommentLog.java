package com.biz.nbcp.domain.commentlog;

import com.biz.nbcp.domain.commentlog.dto.CommentLogRequestDto;
import jakarta.persistence.*;
import lombok.AllArgsConstructor;
import lombok.Builder;
import lombok.NoArgsConstructor;

@Entity
@NoArgsConstructor
@AllArgsConstructor
@Builder
public class CommentLog {

    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    private Long id;

    @Column(length = 20)
    private String userId;

    @Column(length = 100)
    private String blogUrl;

    @Column(length = 1000)
    private String comment;

    public static CommentLog from(CommentLogRequestDto dto) {
        return CommentLog.builder()
                .userId(dto.getUserId())
                .blogUrl(dto.getBlogUrl())
                .comment(dto.getComment())
                .build()
                ;
    }

}
