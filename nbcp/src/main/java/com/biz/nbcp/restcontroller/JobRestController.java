package com.biz.nbcp.restcontroller;

import com.biz.nbcp.dto.response.ApiResponseDto;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;

@RestController
@RequestMapping("/api/job")
public class JobRestController {

    @PostMapping("/start")
    public ResponseEntity<ApiResponseDto<Void>> startJob() {
        return ResponseEntity.ok(new ApiResponseDto<>(true, null, "성공"));
    }
}
