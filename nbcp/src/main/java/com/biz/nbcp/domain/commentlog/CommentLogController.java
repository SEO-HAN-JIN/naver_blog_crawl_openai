package com.biz.nbcp.domain.commentlog;

import com.biz.nbcp.domain.commentlog.dto.CommentLogRequestDto;
import lombok.RequiredArgsConstructor;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestBody;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;

@RestController
@RequiredArgsConstructor
@RequestMapping("/api/comment-logs")
public class CommentLogController {

    private final CommentLogService commentLogService;

    @PostMapping
    public void save(@RequestBody CommentLogRequestDto commentLogRequestDto) {
        commentLogService.save(commentLogRequestDto);
    }
}
