package com.biz.nbcp.domain;

import jakarta.persistence.*;

@Entity
public class CommentLog {

    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    @Column(name = "comment_log_id")
    private Long id;

    @Column(length = 20)
    private String userId;

    @Column(length = 100)
    private String blogUrl;

    @Column(length = 1000)
    private String comment;

}
