package com.biz.nbcp.job;

import com.biz.nbcp.common.dto.api.ApiResponseDto;
import com.biz.nbcp.job.dto.JobRequestDto;
import lombok.RequiredArgsConstructor;
import org.springframework.http.HttpStatus;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestBody;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;

import java.io.IOException;

@RestController
@RequiredArgsConstructor
@RequestMapping("/api/job")
public class JobController {

    private final JobService jobService;

    @PostMapping
    public ResponseEntity<?> runJob(@RequestBody JobRequestDto dto) throws IOException, InterruptedException {
        int result = jobService.runJob(dto);

        if (result == 0) {
            return new ResponseEntity<>(new ApiResponseDto<>(true, null, "성공"), HttpStatus.OK);
        } else {
            return new ResponseEntity<>(new ApiResponseDto<>(false, null, "실패"), HttpStatus.BAD_REQUEST);
        }
    }
}
