package com.biz.nbcp.job;

import com.biz.nbcp.job.dto.JobRequestDto;
import lombok.extern.slf4j.Slf4j;
import org.springframework.beans.factory.annotation.Value;
import org.springframework.stereotype.Service;

import java.io.File;
import java.io.IOException;

@Service
@Slf4j
public class JobService {

    @Value("${docker.image-name}")
    private String imageName;

    public int runJob(JobRequestDto dto) throws IOException, InterruptedException {

        // 1. 이미지 존재 확인
        ProcessBuilder checkImage = new ProcessBuilder("docker", "image", "inspect", imageName);
        Process checkProcess = checkImage.start();
        int checkResult = checkProcess.waitFor();

        // 2. 이미지가 없으면 빌드
        if (checkResult != 0) {
            log.info("도커 이미지가 존재하지 않음..");
            log.info("도커 빌드 시작..");

            ProcessBuilder build = new ProcessBuilder("docker", "build", "-t", imageName, ".");
            build.directory(new File("src/comment_job"));
            Process buildProcess = build.inheritIO().start();
            int buildExitCode = buildProcess.waitFor();
            if (buildExitCode != 0) {
                throw new RuntimeException("도커 이미지 빌드 실패");
            }
        } else {
            log.info("도커 이미지 존재..");
        }


        log.info("도커 컨테이너 실행..");
        // 3. 컨테이너 실행
        ProcessBuilder run = new ProcessBuilder("docker", "run", imageName);
        run.directory(new File("src/comment_job"));
        Process runProcess = run.inheritIO().start();
        int runExitCode = runProcess.waitFor();
        if (runExitCode != 0) {
            throw new RuntimeException("도커 컨테이너 실행 실패");
        }

        return runExitCode;
    }
}
