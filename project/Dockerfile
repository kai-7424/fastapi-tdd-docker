# pull official base image (已自带 uv 的 Astral 官方镜像)
FROM ghcr.io/astral-sh/uv:python3.13-bookworm-slim

# set working directory
RUN mkdir -p /usr/src/app
WORKDIR /usr/src/app

# set environment variables
ENV PYTHONUNBUFFERED=1 \
    UV_COMPILE_BYTECODE=1 \
    UV_LINK_MODE=copy \
    COMPOSE_CONVERT_WINDOWS_PATHS=1

# install python dependencies
COPY pyproject.toml uv.lock ./
RUN uv sync --frozen --no-install-project

# add app
COPY . .
RUN uv sync --frozen

# 把虚拟环境加进 PATH，命令才能找得到
ENV PATH="/usr/src/app/.venv/bin:$PATH"

EXPOSE 8000
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]