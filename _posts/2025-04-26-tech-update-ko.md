# 🛠️ 2025-04-26 기술 업데이트 요약

## 🔹 Kubernetes - Kubernetes v1.33: User Namespaces enabled by default!
Kubernetes v1.33 버전부터는 사용자 네임스페이스가 기본적으로 활성화됩니다. 이는 포드가 사용자 네임스페이스를 사용할 수 있도록 선택할 수 있다는 것을 의미합니다. 사용자 네임스페이스는 컨테이너와 호스트의 UID/GID를 분리하여 보안을 강화합니다. 이를 통해 컨테이너 간의 횡적 이동을 방지하고, 호스트로부터의 격리를 증가시키며, 새로운 사용 사례를 가능하게 합니다. 사용자 네임스페이스는 특히 루트 권한 없이도 특정 애플리케이션을 실행할 수 있어 보안성을 높입니다. Kubernetes v1.33에서는 추가적인 설정 없이도 이 기능을 사용할 수 있으며, 관련 요구 사항과 구성 방법은 공식 문서에서 확인할 수 있습니다.
👉 [자세히 보기](https://kubernetes.io/blog/2025/04/25/userns-enabled-by-default/)

## 🔹 Spring Boot - Spring Boot 3.5.0-RC1 available now
Spring Boot 팀은 버전 3.5.0-RC1을 발표했습니다. 이번 릴리스에는 133개의 개선 사항, 문서 개선, 종속성 업그레이드, 버그 수정이 포함되어 있으며, Docker의 자격 증명 저장소 및 도우미 지원, 설정 속성 바인딩 성능 향상, 애노테이션 기반 필터 및 서블릿 등록, 빈의 백그라운드 초기화 자동 구성, 전역 WebClient 설정을 위한 속성 등 새로운 기능들이 추가되었습니다. 자세한 내용과 업그레이드 지침은 릴리스 노트를 참조하세요. 기여를 원하시는 분은 기여에 적합한 이슈 태그를 확인하거나, 일반적인 질문은 Stack Overflow에서 할 수 있습니다.
👉 [자세히 보기](https://spring.io/blog/2025/04/25/spring-boot-3-5-0-RC1-available-now)

## 🔹 Docker - How to build and deliver an MCP server for production
이 기술 블로그 글은 MCP(Model Context Protocol) 서버를 구축하고 프로덕션 환경에 배포하는 방법에 대해 다룹니다. 2024년 12월, Anthropic과 함께 AI 에이전트를 활용한 도구 실행을 위한 완전히 새로운 사양인 MCP를 소개하는 블로그를 발표한 이후, 개발자들이 Agentic AI와 함께 MCP를 사용하여 도구를 구축, 공유 및 실행하려는 수요가 급증했습니다. 이 글은 Docker를 사용하여 MCP 서버를 프로덕션 환경에 배포하는 과정을 설명합니다.
👉 [자세히 보기](https://www.docker.com/blog/build-to-prod-mcp-servers-with-docker/)

## 🔹 Java - Finalizing the Java On-ramp - Inside Java Newscast #90
블로그 글 요약: Java 25 릴리스에서 중요한 변화가 예상됩니다. 이번 Inside Java Newscast 에피소드에서는 Java 25에서 최종 확정될 'Paving the On-ramp' 기능 세트에 대해 살펴봅니다. 또한, Java를 배우고자 하는 사람들과 Java 교육자들을 위한 새로운 웹사이트 'lear.java'의 출시 소식도 다룹니다.
👉 [자세히 보기](https://inside.java/2025/04/24/ijn-ep-90/)

## 🔹 Golang - More predictable benchmarking with testing.B.Loop
해당 글은 Go 1.24 버전에서 개선된 benchmarking 기능인 `testing.B.Loop`에 대해 다루고 있습니다. 이 기능은 보다 예측 가능한 벤치마크 반복 실행을 가능하게 하여, 성능 테스트의 일관성과 정확성을 높이는 데 기여합니다.
👉 [자세히 보기](https://go.dev/blog/testing-b-loop)

## 🔹 Helm - Helm @ KubeCon + CloudNativeCon EU '25
블로그 글 요약: Helm 팀은 2025년 4월 1일부터 4일까지 영국 런던에서 열리는 KubeCon + CloudNativeCon EU '25에 참가합니다. 올해 말 출시 예정인 Helm 4에 대한 논의에 참여할 수 있는 기회가 제공되며, 프로젝트 파빌리온에 있는 Helm 부스와 발표 세션에서 유지 관리자들과 대화할 수 있습니다. 주간 동안 진행되는 Helm 관련 활동에 대한 자세한 내용은 블로그에서 확인할 수 있습니다.
👉 [자세히 보기](https://helm.sh/blog/helm-at-kubecon-eu-25/)

