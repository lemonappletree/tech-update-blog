# 🛠️ 2025-11-19 기술 업데이트 요약

## 🔹 Kubernetes - Ingress NGINX Retirement: What You Need to Know
Kubernetes SIG Network와 보안 대응 위원회는 Ingress NGINX의 퇴역 계획을 발표했습니다. Ingress NGINX는 2026년 3월까지 최선의 노력을 다해 유지 관리되며, 이후로는 추가 릴리스, 버그 수정 또는 보안 취약점 해결 업데이트가 제공되지 않습니다. 기존 배포는 계속 작동하며 설치 아티팩트는 유지됩니다. 사용자는 Gateway API 등 대안으로의 마이그레이션을 권장합니다. Ingress NGINX는 Kubernetes 프로젝트 초기부터 유연성과 기능성 때문에 인기를 끌었지만, 유지 관리 인력의 부족과 기술 부채로 인해 퇴역이 결정되었습니다. 사용자 안전을 우선시하기 위해 SIG Network와 보안 대응 위원회는 프로젝트의 종료를 결정했습니다. Ingress NGINX 사용자들은 즉시 대안으로의 전환을 시작해야 합니다.
👉 [자세히 보기](https://kubernetes.io/blog/2025/11/11/ingress-nginx-retirement/)

## 🔹 Spring Boot - OpenTelemetry with Spring Boot
이 블로그 글은 Spring Boot와 OpenTelemetry의 통합을 다루고 있습니다. 현대 클라우드 네이티브 아키텍처에서 관측 가능성은 필수 요소이며, OpenTelemetry는 벤더 중립적 오픈 소스 프레임워크로서 메트릭, 트레이스, 로그 등의 데이터를 수집, 처리, 내보낼 수 있도록 돕습니다. Spring Boot와 OpenTelemetry를 통합하는 방법에는 여러 가지가 있으며, 이 글에서는 세 가지 옵션을 제시합니다: OpenTelemetry Java Agent 사용, 3rd-party OpenTelemetry Spring Boot Starter 사용, 그리고 Spring 팀의 OpenTelemetry Spring Boot Starter 사용입니다.

Spring Boot 4.0에서는 OpenTelemetry Starter가 도입되며, 이는 Micrometer를 통해 메트릭과 트레이스를 OTLP 포맷으로 내보내는 것을 지원합니다. 또한 로그를 OTLP 포맷으로 내보내기 위한 설정 방법도 설명합니다. 컨텍스트 전파 문제와 관련하여 Trace ID를 HTTP 헤더에 포함시키는 방법과, 멀티 스레드 환경에서 컨텍스트를 보존하는 방법도 다룹니다. 

마지막으로, Grafana를 사용한 시연을 통해 로그, 트레이스, 메트릭이 어떻게 시각화될 수 있는지를 보여주며, Spring Boot의 OpenTelemetry 통합이 얼마나 강력한지를 설명합니다.
👉 [자세히 보기](https://spring.io/blog/2025/11/18/opentelemetry-with-spring-boot)

## 🔹 Docker - Docker + Unsloth: Build Custom Models, Faster
블로그 글은 Docker와 Unsloth를 사용하여 맞춤형 모델을 더 빠르게 구축하는 방법에 대해 설명합니다. 로컬에서 AI 모델을 실행하는 것은 여전히 어렵고, 올바른 종속성을 갖춘 상태로 자신의 기기에서 실행하는 데는 시간이 많이 걸리며 불안정하고 일관성이 부족합니다. 이러한 어려움은 모델 생성 및 최적화, 즉 미세 조정과 양자화의 효율성을 높이는 것과 관련이 있습니다. Docker와 Unsloth는 이러한 문제를 해결하는 데 도움을 줍니다.
👉 [자세히 보기](https://www.docker.com/blog/docker-unsloth-build-custom-models-faster/)

## 🔹 Java - JEP targeted to JDK 26: 524: PEM Encodings of Cryptographic Objects (Second Preview)
제목이 "JEP targeted to JDK 26: 524: PEM Encodings of Cryptographic Objects (Second Preview)"인 기술 블로그 글은 JDK 26에 목표를 둔 JEP 524에 대한 내용을 다루고 있습니다. 이 JEP는 암호화 객체의 PEM 인코딩을 다루며, 이번이 두 번째 미리보기 버전입니다. 자세한 내용은 제공된 링크에서 확인할 수 있습니다.
👉 [자세히 보기](https://inside.java/2025/11/17/jep524-target-jdk26/)

## 🔹 Golang - Go’s Sweet 16
블로그 글 "Go’s Sweet 16"은 Go 프로그래밍 언어의 16번째 생일을 축하하는 내용입니다. 이 글은 Go 언어의 발전과 그동안의 주요 성과를 되돌아보며, 커뮤니티와 개발자들에게 감사를 표하고 있습니다. Go의 미래에 대한 기대감과 함께, 다양한 프로젝트와 기여자들의 노력을 강조하고 있습니다.
👉 [자세히 보기](https://go.dev/blog/16years)

