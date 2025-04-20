package com.biz.nbcp.domain.commentlog;

import com.biz.nbcp.domain.commentlog.dto.CommentLogRequestDto;
import lombok.RequiredArgsConstructor;
import org.springframework.stereotype.Service;

@Service
@RequiredArgsConstructor
public class CommentLogService {

    private final CommentLogRepository commentLogRepository;

    public void save(CommentLogRequestDto dto) {
        commentLogRepository.save(CommentLog.from(dto));
    }
}
