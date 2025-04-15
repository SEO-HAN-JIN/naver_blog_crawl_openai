package com.biz.nbcp.dto.response;

import lombok.Getter;
import lombok.RequiredArgsConstructor;

@RequiredArgsConstructor
@Getter
public class ApiResponseDto<T> {
    private final boolean success;
    private final T data;
    private final String message;

}
