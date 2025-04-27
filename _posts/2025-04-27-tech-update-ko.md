# 🛠️ 2025-04-27 기술 업데이트 요약

## 🔹 Kubernetes - Kubernetes v1.33: User Namespaces enabled by default!
Kubernetes v1.33 버전에서는 사용자 네임스페이스 기능이 기본으로 활성화되었습니다. 이는 요구 사항이 충족될 경우, 사용자 네임스페이스를 사용하여 pod를 실행할 수 있다는 것을 의미합니다. 사용자 네임스페이스는 컨테이너 내에서 UID와 GID를 호스트와 분리하여 각 컨테이너가 서로 다른 UID와 GID로 매핑되도록 하여 보안성을 높입니다. 이로 인해 컨테이너 탈출 시 호스트에서의 권한이 제한되며, 새로운 사용 사례를 가능하게 합니다. 이 블로그 글은 사용자 네임스페이스의 중요성과 Kubernetes에서의 활용 방법, 그리고 관련된 질문들에 대한 답변을 제공합니다. 사용자 네임스페이스를 통해 애플리케이션 코드를 변경하지 않고도 비루트 권한으로 실행할 수 있습니다.
👉 [자세히 보기](https://kubernetes.io/blog/2025/04/25/userns-enabled-by-default/)

## 🔹 Spring Boot - Spring Boot 3.5.0-RC1 available now
Spring Boot 3.5.0-RC1 버전이 출시되었습니다. 이번 릴리스에는 133개의 개선 사항, 문서 업데이트, 종속성 업그레이드 및 버그 수정이 포함되어 있습니다. 주요 새로운 기능으로는 Docker의 자격 증명 저장소 및 도우미 지원, 구성 속성 바인딩 성능 개선, 애노테이션 기반 필터 및 서블릿 등록, 빈의 백그라운드 초기화 자동 구성, 전역 WebClient 구성을 위한 속성 등이 있습니다. 더 자세한 내용과 업그레이드 지침은 릴리스 노트를 참조하세요. 기여하고 싶다면, 기여하기 이상적인 태그가 붙은 이슈를 확인해보세요. 일반적인 질문은 Stack Overflow에서 spring-boot 태그를 사용해 문의할 수 있습니다.
👉 [자세히 보기](https://spring.io/blog/2025/04/25/spring-boot-3-5-0-RC1-available-now)

## 🔹 Docker - How to build and deliver an MCP server for production
이 기술 블로그 글은 AI 에이전트와 함께 도구를 실행하기 위한 새로운 사양인 모델 컨텍스트 프로토콜(MCP)에 대해 설명합니다. 2024년 12월에 Anthropic과 함께 MCP에 관한 블로그를 발표했으며, 이후 개발자들이 에이전틱 AI와 함께 도구를 구축, 공유, 실행하려는 수요가 급증했다고 합니다. 이 글은 Docker를 사용하여 MCP 서버를 프로덕션 환경으로 구축하고 배포하는 방법을 다루고 있습니다.
👉 [자세히 보기](https://www.docker.com/blog/build-to-prod-mcp-servers-with-docker/)

## 🔹 Java - Finalizing the Java On-ramp - Inside Java Newscast #90
블로그 글 요약: Java 25 버전에서 중요한 변화가 있을 예정입니다. 'Paving the On-ramp' 기능 세트가 Java 25에서 최종 확정될 예정이며, Java 학습을 원하는 사람들과 Java를 가르치는 사람들을 위한 새로운 웹사이트 lear.java의 출시에 대해서도 다룹니다.
👉 [자세히 보기](https://inside.java/2025/04/24/ijn-ep-90/)

## 🔹 Golang - More predictable benchmarking with testing.B.Loop
이 기술 블로그 글은 Go 1.24에서 도입된 `testing.B.Loop` 기능을 중심으로 설명하고 있습니다. 이 새로운 기능은 벤치마크 테스트에서 반복 실행을 더 예측 가능하게 만들어주며, 개발자들이 보다 정확한 성능 측정을 할 수 있도록 돕습니다. `testing.B.Loop`를 활용하면 벤치마크의 반복 실행을 더욱 간편하게 관리할 수 있어, 코드 성능 최적화에 기여할 수 있습니다.
👉 [자세히 보기](https://go.dev/blog/testing-b-loop)

## 🔹 Helm - Helm @ KubeCon + CloudNativeCon EU '25
제목: Helm @ KubeCon + CloudNativeCon EU '25

요약: Helm 팀이 4월 1일부터 4일까지 영국 런던에서 열리는 KubeCon + CloudNativeCon EU '25에 참석합니다. 올해 말 출시 예정인 Helm 4에 대한 논의에 참여할 수 있는 기회가 마련되어 있으며, 팀 유지 관리자들과의 대화 세션 및 프로젝트 파빌리온의 Helm 부스에서도 만날 수 있습니다. 주간 동안의 모든 Helm 관련 활동에 대한 자세한 내용은 아래 링크를 참조하세요.
👉 [자세히 보기](https://helm.sh/blog/helm-at-kubecon-eu-25/)

