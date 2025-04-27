package com.biz.nbcp.common.dto.api;

import lombok.Getter;
import lombok.RequiredArgsConstructor;

@RequiredArgsConstructor
@Getter
public class ApiResponseDto<T> {
    private final boolean success;
    private final T data;
    private final String message;

}
