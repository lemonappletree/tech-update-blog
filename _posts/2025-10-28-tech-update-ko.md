# 🛠️ 2025-10-28 기술 업데이트 요약

## 🔹 Kubernetes - 7 Common Kubernetes Pitfalls (and How I Learned to Avoid Them)
이 블로그 글은 Kubernetes 사용 시 흔히 저지르는 7가지 실수와 이를 피하는 방법에 대해 다룹니다. Kubernetes는 강력하지만 때로는 좌절감을 줄 수 있습니다. 이 글에서는 Pod 자원의 요청 및 제한 설정 누락, 라이브니스 및 레디니스 프로브 과소평가, 로그 관리 소홀, 개발 및 프로덕션 환경의 동일 처리, 오래된 리소스 방치, 네트워킹의 과도한 복잡화, 보안 및 RBAC 부족 등 7가지 주요 실수를 소개하고, 각 실수를 피하기 위한 팁을 제공합니다. 예를 들어, 자원 요청과 제한을 설정하여 클러스터 관리 효율성을 높이고, 적절한 프로브를 사용해 컨테이너의 상태를 모니터링하며, 중앙 집중화된 로그 관리와 환경별 설정 최적화를 통해 이러한 문제를 방지할 수 있습니다. 최종적으로 이 글은 Kubernetes의 공식 문서와 커뮤니티 Slack을 통해 더 깊이 있는 학습을 권장하고 있습니다.
👉 [자세히 보기](https://kubernetes.io/blog/2025/10/20/seven-kubernetes-pitfalls-and-how-to-avoid/)

## 🔹 Spring Boot - Prompt Caching Support in Spring AI with Anthropic Claude
이 블로그 글은 대규모 언어 모델 API 비용을 절감하기 위한 방법으로 Anthropic Claude의 프롬프트 캐싱을 소개합니다. Spring AI는 이러한 캐싱을 통해 프롬프트를 효율적으로 재사용할 수 있도록 지원합니다. 프롬프트 캐싱은 동일한 내용의 요청이 반복될 때 비용을 절감하고 응답 지연 시간을 줄이는 데 효과적입니다. 캐시 전략에는 SYSTEM_ONLY, TOOLS_ONLY, SYSTEM_AND_TOOLS, CONVERSATION_HISTORY 등이 있으며, 각 전략은 특정 사용 사례에 맞게 설계되었습니다. 이를 통해 요청의 일관성을 유지하고 캐시 히트율을 극대화할 수 있습니다. Spring AI는 이러한 캐싱 전략을 자동으로 관리하여 개발자가 쉽게 구현할 수 있도록 돕습니다.
👉 [자세히 보기](https://spring.io/blog/2025/10/27/spring-ai-anthropic-prompt-caching-blog)

## 🔹 Docker - How to Connect MCP Servers to Claude Desktop with Docker MCP Toolkit
이 블로그 글은 Claude Desktop을 개발 파트너로 활용하기 위해 MCP 서버를 연결하는 방법에 대해 설명합니다. Docker MCP Toolkit을 사용하면 안전하고 보안이 유지된 상태로 로컬 기기에 접근하지 않고도 Claude를 실제 개발 도구와 연결할 수 있습니다. 이 글은 Claude Desktop을 실제 개발 도구와 연결하는 방법을 찾고 있는 사람들에게 필요한 정보를 제공합니다.
👉 [자세히 보기](https://www.docker.com/blog/connect-mcp-servers-to-claude-desktop-with-mcp-toolkit/)

## 🔹 Java - Episode 41 “From Cowboy Mode to Careful Stewardship” with Mark Reinhold
블로그 글은 Nicolai Parlog이 자바 플랫폼의 수석 설계자인 Mark Reinhold와의 대화를 다루고 있습니다. Mark Reinhold는 자바 발전에 거의 30년의 경험을 가지고 있으며, 이 글에서는 자바의 초기 '카우보이 모드'에서부터 현재의 신중한 관리 방식으로의 전환 과정을 설명합니다. 
👉 [자세히 보기](https://inside.java/2025/10/27/podcast-041/)

## 🔹 Golang - Flight Recorder in Go 1.25
Go 1.25 버전에서는 진단 도구에 새로운 기능인 "비행 기록"이 도입되었습니다. 이 기능은 프로그램 실행 중 발생하는 다양한 이벤트와 상태를 기록하여 문제 해결과 성능 최적화에 도움을 줍니다. 구체적인 사용 방법과 장점에 대해서는 블로그 원문에서 자세히 설명되어 있습니다.
👉 [자세히 보기](https://go.dev/blog/flight-recorder)

## 🔹 Helm - Helm Turns 10
블로그 글은 Helm의 10주년을 기념하는 내용을 담고 있습니다. Helm은 Kubernetes 1.1.0이 출시된 직후 진행된 해커톤에서 탄생했습니다. 초기 코드베이스는 helm-classic Git 저장소에 있으며, 이는 Helm v1의 원본입니다. 이후 Helm은 Deployment Manager와 통합되어 Kubernetes 프로젝트로 포함되었습니다.
👉 [자세히 보기](https://helm.sh/blog/helm-turns-ten/)

