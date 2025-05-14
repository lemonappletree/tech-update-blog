# 🛠️ 2025-05-14 기술 업데이트 요약

## 🔹 Kubernetes - Kubernetes v1.33: Job's Backoff Limit Per Index Goes GA
이 블로그 글은 Kubernetes v1.33에서 '인덱스별 백오프 제한(Backoff Limit Per Index)' 기능이 일반 제공(GA)에 도달했음을 설명합니다. 이 기능은 Kubernetes 작업(Job)에서 인덱스별로 실패를 제어할 수 있도록 도와줍니다. 특히 독립적인 인덱스로 구성된 작업에서 유용하며, 각 인덱스마다 재시도 횟수를 설정할 수 있습니다. 이를 통해 특정 인덱스의 빠른 실패가 전체 작업의 실패 허용 한도를 소진하지 않도록 합니다. 또한, 작업의 전체 실패 인덱스 수를 제한하거나 실패 인덱스를 감지하는 메커니즘도 제공합니다. 이 기능은 Kubernetes batch 작업 그룹과 SIG Apps 커뮤니티가 협력하여 개발한 결과물입니다.
👉 [자세히 보기](https://kubernetes.io/blog/2025/05/13/kubernetes-v1-33-jobs-backoff-limit-per-index-goes-ga/)

## 🔹 Spring Boot - Spring AI 1.0.0 RC1 Released
Spring AI 1.0.0 RC1 버전이 출시되었습니다. 이 버전은 안정적인 출시 전 마지막 변경 사항, 버그 수정 및 기능 추가가 포함되어 있으며, GA 버전은 2025년 5월 20일에 출시될 예정입니다. 문서 개선과 버그 수정에 집중할 계획입니다. 이번 출시를 기념하여 AI 생성 음악 플레이리스트에 새로운 곡이 추가되었습니다.

주요 변경 사항으로는 채팅 메모리 및 자문 기능의 변경, 독립적인 템플릿 사용, 채팅 메모리 저장소 명명 규칙 표준화 등이 있습니다. 새로운 기능으로는 DeepSeek 통합, Azure OpenAI 개선, OpenAI 기능 강화, Vertex AI Gemini 지원 등이 포함되었습니다. 문서 처리 및 도구 호출, 메모리 관리, 관측 가능성 측면에서도 여러 개선이 이루어졌습니다. 다양한 기여자들이 이번 릴리스에 참여했습니다.
👉 [자세히 보기](https://spring.io/blog/2025/05/13/spring-ai-1-0-0-RC1-released)

## 🔹 Docker - Securing Model Context Protocol: Safer Agentic AI with Containers
이 기술 블로그 글은 모델 컨텍스트 프로토콜(MCP)의 보안 문제와 이를 해결하기 위한 방법에 대해 다룹니다. MCP 도구는 현재 초기 사용자들 사이에서 주로 사용되고 있지만, 점점 더 많은 사람들이 이를 채택하고 있습니다. 그러나 MCP의 성장과 함께 보안 문제도 더 중요해지고 있습니다. MCP 도구는 에이전트의 자율성을 증가시켜 사용자 기대와 에이전트 행동 간의 불일치나 통제되지 않은 실행과 관련된 새로운 위험을 초래할 수 있습니다. 이러한 시스템은 또한 새로운 보안 문제를 제기합니다. 이 글에서는 이러한 문제를 해결하기 위해 컨테이너를 활용한 MCP 보안 강화 방안을 제시합니다.
👉 [자세히 보기](https://www.docker.com/blog/whats-next-for-mcp-security/)

## 🔹 Java - JEP targeted to JDK 25: 505: Structured Concurrency (5th Preview)
이 기술 블로그 글은 JDK 25에 포함될 예정인 JEP 505에 대해 다루고 있습니다. JEP 505는 "구조적 동시성"이라는 주제로, 이번이 다섯 번째 프리뷰입니다. 이 JEP는 자바 프로그래밍 언어에서 동시성을 보다 구조적으로 관리할 수 있도록 개선하는 것을 목표로 하고 있습니다. 자세한 내용은 링크를 통해 확인할 수 있습니다.
👉 [자세히 보기](https://inside.java/2025/05/12/jep505-target-jdk25/)

## 🔹 Golang - More predictable benchmarking with testing.B.Loop
이 블로그 글은 Go 1.24 버전에서의 개선된 벤치마크 루프에 대해 다루고 있습니다. 새로운 `testing.B.Loop` 기능은 더 예측 가능한 벤치마킹을 가능하게 하여 개발자들이 성능 테스트를 보다 효율적으로 수행할 수 있도록 돕습니다. 이는 벤치마크의 일관성을 높이고, 성능 최적화 작업을 쉽게 해줍니다.
👉 [자세히 보기](https://go.dev/blog/testing-b-loop)

## 🔹 Helm - Helm @ KubeCon + CloudNativeCon EU '25
제목: Helm @ KubeCon + CloudNativeCon EU '25

요약: Helm 팀이 2025년 4월 1일부터 4일까지 영국 런던에서 열리는 KubeCon + CloudNativeCon EU '25에 참가합니다. 올해 말 출시 예정인 Helm 4에 대한 논의가 진행될 예정이니, 발표 세션과 프로젝트 파빌리온의 Helm 부스에서 유지 관리자들과의 대화에 참여해 보세요. 주간 동안 진행되는 모든 Helm 관련 활동에 대한 자세한 내용은 블로그에서 확인할 수 있습니다.
👉 [자세히 보기](https://helm.sh/blog/helm-at-kubecon-eu-25/)

