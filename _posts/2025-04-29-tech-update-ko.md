# 🛠️ 2025-04-29 기술 업데이트 요약

## 🔹 Kubernetes - Kubernetes v1.33: HorizontalPodAutoscaler Configurable Tolerance
이 기술 블로그 글은 Kubernetes 1.33에서 도입된 새로운 알파 기능인 "HorizontalPodAutoscaler Configurable Tolerance"에 대해 설명합니다. Horizontal Pod Autoscaling(HPA)은 리소스 사용량에 따라 워크로드의 레플리카 수를 자동으로 조정하는 Kubernetes의 기능입니다. 기존에는 클러스터 전역적으로 10%의 기본 허용 오차가 적용되어 작은 메트릭 변동으로 인한 빈번한 레플리카 생성 및 삭제를 방지했습니다. 그러나 이 값은 대규모 배포에는 적합하지 않았기 때문에, 커뮤니티에서는 이 값을 조정할 수 있는 기능을 요청해왔습니다. Kubernetes 1.33에서는 HPAConfigurableTolerance 기능 게이트를 활성화하여 원하는 허용 오차를 설정할 수 있게 되었습니다. 이로 인해 확장 및 축소 시의 허용 오차를 개별적으로 설정할 수 있으며, 예를 들어 확장 시에는 빠르게 반응하도록 작은 허용 오차를, 축소 시에는 큰 허용 오차를 설정할 수 있습니다.
👉 [자세히 보기](https://kubernetes.io/blog/2025/04/28/kubernetes-v1-33-hpa-configurable-tolerance/)

## 🔹 Spring Boot - Spring Boot 3.5.0-RC1 available now
Spring Boot 3.5.0-RC1 버전이 출시되었습니다. 이번 릴리스에는 133개의 기능 개선, 문서 향상, 종속성 업그레이드, 버그 수정이 포함되어 있습니다. 주요 새로운 기능으로는 Docker의 자격 증명 저장소 및 도우미 지원, 설정 속성 바인딩 성능 개선, 애노테이션 기반 필터 및 서블릿 등록, 빈의 백그라운드 초기화 자동 구성, 전역 WebClient 구성 속성이 있습니다. 자세한 내용과 업그레이드 지침은 릴리스 노트를 참고하세요. 기여를 원하신다면 GitHub의 'ideal for contribution' 태그를 확인하거나, Stack Overflow에서 spring-boot 태그를 사용하여 질문할 수 있습니다.
👉 [자세히 보기](https://spring.io/blog/2025/04/25/spring-boot-3-5-0-RC1-available-now)

## 🔹 Docker - How to build and deliver an MCP server for production
이 블로그 글은 2024년 12월에 Anthropic과 함께 발표된 새로운 사양인 Model Context Protocol(MCP)을 사용하여 AI 에이전트로 도구를 실행하는 방법에 대해 설명합니다. 이후 개발자들이 MCP를 활용하여 도구를 구축하고 공유하며 실행하려는 관심이 급증했습니다. 이 글은 Docker를 사용하여 MCP 서버를 프로덕션 환경에 구축하고 전달하는 방법에 대해 다룹니다.
👉 [자세히 보기](https://www.docker.com/blog/build-to-prod-mcp-servers-with-docker/)

## 🔹 Java - Finalizing the Java On-ramp - Inside Java Newscast #90
블로그 글 요약: Java 25 릴리스에서는 큰 변화가 있을 예정입니다. 이번 Inside Java Newscast 에피소드에서는 Java 25에서 최종 확정될 'Paving the On-ramp' 기능 세트를 살펴봅니다. 또한, Java를 배우고자 하는 사람들과 Java를 가르치는 사람들을 위해 새로 런칭된 웹사이트 lear.java에 대해서도 알아봅니다.
👉 [자세히 보기](https://inside.java/2025/04/24/ijn-ep-90/)

## 🔹 Golang - More predictable benchmarking with testing.B.Loop
해당 블로그 글은 Go 1.24 버전에서 개선된 벤치마크 루프에 대해 다루고 있습니다. Go 언어의 새로운 기능인 `testing.B.Loop`를 통해 벤치마크 테스트의 예측 가능성이 향상되었으며, 이를 통해 더 안정적이고 신뢰할 수 있는 성능 측정이 가능해졌다는 내용을 요약하고 있습니다.
👉 [자세히 보기](https://go.dev/blog/testing-b-loop)

## 🔹 Helm - Helm @ KubeCon + CloudNativeCon EU '25
제목: Helm @ KubeCon + CloudNativeCon EU '25

Helm 팀이 2025년 4월 1일부터 4일까지 영국 런던에서 열리는 KubeCon + CloudNativeCon EU에 참가합니다. 올해 말 출시 예정인 Helm 4에 대한 논의를 위해 유지 관리자들과의 대화에 참여하고, 프로젝트 파빌리온에 있는 Helm 부스를 방문해보세요. 주간 동안 진행될 모든 Helm 관련 활동에 대한 자세한 내용은 링크를 참조하세요.
👉 [자세히 보기](https://helm.sh/blog/helm-at-kubecon-eu-25/)

