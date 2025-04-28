# 🛠️ 2025-04-28 기술 업데이트 요약

## 🔹 Kubernetes - Kubernetes v1.33: User Namespaces enabled by default!
Kubernetes v1.33 버전에서는 사용자 네임스페이스 기능이 기본으로 활성화되었습니다. 이는 스택 요구 사항이 충족될 경우, 포드가 사용자 네임스페이스를 선택적으로 사용할 수 있음을 의미합니다. 이 기능을 사용하기 위해 별도의 Kubernetes 기능 플래그를 활성화할 필요가 없습니다. 사용자 네임스페이스는 리눅스 커널 기능으로, 컨테이너의 UID와 GID를 호스트와 별도로 격리하여 보안성을 높이는 데 기여합니다. 이 기능을 통해 컨테이너는 호스트에서 비특권 사용자로 실행되며, 이는 보안 취약점(CVE) 완화에도 도움을 줍니다. 이러한 사용자 네임스페이스는 특히 중첩된 컨테이너를 실행하거나 특권 작업이 필요한 애플리케이션을 안전하게 실행하는 데 유용합니다. Kubernetes 문서에서 자세한 설정 방법 및 요구 사항을 확인할 수 있습니다.
👉 [자세히 보기](https://kubernetes.io/blog/2025/04/25/userns-enabled-by-default/)

## 🔹 Spring Boot - Spring Boot 3.5.0-RC1 available now
Spring Boot 3.5.0-RC1 버전이 출시되었습니다. 이번 릴리스는 133개의 개선사항, 문서 업데이트, 종속성 업그레이드 및 버그 수정을 포함하고 있습니다. 주요 기능으로는 Docker의 자격 증명 저장소 지원, 구성 속성 바인딩 성능 개선, 애노테이션 기반 필터 및 서블릿 등록, 빈의 백그라운드 초기화를 위한 자동 구성, 글로벌 WebClient 구성 속성 등이 있습니다. 자세한 내용과 업그레이드 방법은 릴리스 노트를 참고하세요. 기여를 원하시는 분들은 GitHub의 "ideal for contribution" 태그를 확인하거나, Stack Overflow에서 질문할 수 있습니다.
👉 [자세히 보기](https://spring.io/blog/2025/04/25/spring-boot-3-5-0-RC1-available-now)

## 🔹 Docker - How to build and deliver an MCP server for production
이 기술 블로그 글은 2024년 12월에 Anthropic과 함께 발표한 AI 에이전트를 활용한 도구 실행을 위한 새로운 사양인 모델 컨텍스트 프로토콜(MCP)에 관한 것입니다. 이후 개발자들이 MCP를 사용하여 자신의 도구를 구축, 공유 및 실행하려는 수요가 급증했습니다. 이 글에서는 Docker를 사용하여 MCP 서버를 프로덕션 환경에 구축하고 전달하는 방법에 대해 설명하고 있습니다.
👉 [자세히 보기](https://www.docker.com/blog/build-to-prod-mcp-servers-with-docker/)

## 🔹 Java - Finalizing the Java On-ramp - Inside Java Newscast #90
블로그 글 요약: Java 25 릴리스에서 중요한 변화가 있을 예정입니다. Inside Java Newscast 90화에서는 Java 25에서 최종 확정될 'Paving the On-ramp' 기능 세트를 살펴봅니다. 또한, Java를 배우고 가르치고자 하는 사람들을 위한 새로운 웹사이트 'lear.java'의 출시도 다룹니다.
👉 [자세히 보기](https://inside.java/2025/04/24/ijn-ep-90/)

## 🔹 Golang - More predictable benchmarking with testing.B.Loop
제목: Go 1.24의 더 예측 가능한 벤치마킹

요약: Go 1.24에서는 `testing.B.Loop` 기능을 통해 벤치마크 루프가 개선되었습니다. 이 기능은 벤치마크 테스트의 일관성과 예측 가능성을 높여줍니다.
👉 [자세히 보기](https://go.dev/blog/testing-b-loop)

## 🔹 Helm - Helm @ KubeCon + CloudNativeCon EU '25
제목: Helm @ KubeCon + CloudNativeCon EU '25

요약: Helm 팀이 올해도 KubeCon + CloudNativeCon EU '25에 참가하기 위해 영국 런던으로 향합니다. 이번 행사는 4월 1일부터 4일까지 열립니다. 올해 말 출시 예정인 Helm 4에 대한 논의에 참여하고 싶다면, 우리의 발표 세션과 프로젝트 파빌리온 내 Helm 부스를 방문해보세요. 행사 기간 동안 진행되는 모든 Helm 관련 활동에 대한 자세한 내용은 아래 링크를 참고하세요.
👉 [자세히 보기](https://helm.sh/blog/helm-at-kubecon-eu-25/)

