# 🛠️ 2025-10-12 기술 업데이트 요약

## 🔹 Kubernetes - Introducing Headlamp Plugin for Karpenter - Scaling and Visibility
이 블로그 글은 Karpenter용 Headlamp 플러그인을 소개합니다. Headlamp는 오픈 소스 Kubernetes UI 프로젝트로, 클러스터 자원을 탐색하고 관리하며 디버깅할 수 있도록 합니다. Karpenter는 Kubernetes 오토스케일링 프로젝트로, 클러스터가 빠르고 효율적으로 확장될 수 있도록 돕는 노드 프로비저닝 도구입니다. 새로운 Headlamp Karpenter 플러그인은 Headlamp UI에서 Karpenter의 활동을 실시간으로 볼 수 있게 하여, Kubernetes 객체와의 관계를 보여주고, 실시간 메트릭과 스케일링 이벤트를 표시합니다. 사용자는 프로비저닝 중인 대기 중인 파드를 검사하고, 스케일링 결정을 검토하며, Karpenter가 관리하는 자원을 편집할 수 있습니다. 플러그인은 LFX 멘토 프로젝트의 일환으로 개발되었습니다.

이 플러그인은 Karpenter 자원과 Kubernetes 자원의 관계를 시각화하고, Karpenter 메트릭을 쉽게 볼 수 있도록 하며, 스케일링 결정의 이유를 보여줍니다. 또한, Karpenter 구성의 실시간 편집과 검증 지원이 가능하며, 실시간으로 Karpenter 자원을 추적할 수 있습니다. 플러그인은 AWS와 Azure에서 테스트되었으며, 다른 제공자에 대한 지원은 추가적인 테스트가 필요합니다. 사용법과 피드백 제출 방법에 대한 자세한 내용은 GitHub 리포지토리를 참조하면 됩니다.
👉 [자세히 보기](https://kubernetes.io/blog/2025/10/06/introducing-headlamp-plugin-for-karpenter/)

## 🔹 Spring Boot - A Bootiful Podcast: Spring Security contributor Josh Cummings on the latest-and-greatest in Spring Security 7
이 기술 블로그 글은 Spring Security 기여자이자 유명 인사인 Josh Cummings와의 팟캐스트 인터뷰에 관한 내용입니다. 이번 회차에서는 Spring Security 7의 최신 기능과 개선점에 대해 이야기합니다. Spring Security에 관심 있는 팬들이라면 이 팟캐스트를 통해 유익한 정보를 얻을 수 있을 것입니다.
👉 [자세히 보기](https://spring.io/blog/2025/10/09/a-bootiful-podcast-josh-cummings)

## 🔹 Docker - How to Add MCP Servers to Claude Code with Docker MCP Toolkit
이 기술 블로그 글은 Claude Code와 같은 AI 코딩 도우미가 발전했지만, 여전히 직접 환경에서 행동할 수 없는 한계를 지니고 있음을 설명합니다. Claude Code는 데이터베이스 쿼리를 제안하거나 GitHub 이슈 초안을 작성할 수 있지만, 이를 실행하거나 생성할 수는 없습니다. Docker MCP Toolkit을 사용하여 Claude Code에 MCP 서버를 추가하면 이러한 한계를 극복할 수 있는 방법을 소개합니다.
👉 [자세히 보기](https://www.docker.com/blog/add-mcp-servers-to-claude-code-with-mcp-toolkit/)

## 🔹 Java - “Just Make All Exceptions Unchecked” - Live Q&amp;A from Devoxx
이 기술 블로그 글은 Java의 오류 처리 방식과 관련된 내용으로, 특히 체크드 예외와 언체크드 예외의 구분에 대해 논의합니다. 많은 Java 개발자들이 체크드 예외보다 언체크드 예외를 선호하며, 체크드 예외가 실수였는지를 고민합니다. Stuart Marks와 Nicolai Parlog는 이러한 주제에 대해 Devoxx에서의 라이브 Q&A 세션에서 논의했습니다.
👉 [자세히 보기](https://inside.java/2025/10/09/devoxxstream/)

## 🔹 Golang - Flight Recorder in Go 1.25
Go 1.25에서는 진단 도구 상자에 새로운 도구인 비행 기록 기능이 도입되었습니다. 이 기능은 Go 애플리케이션의 실행 중 발생하는 이벤트를 기록하여 문제 해결 및 성능 최적화에 도움을 줍니다.
👉 [자세히 보기](https://go.dev/blog/flight-recorder)

## 🔹 Helm - Path To Releasing Helm v4
헬름 v4의 첫 번째 알파 버전이 출시되었습니다. 헬름 v4 개발이 막바지에 이른 만큼, 현재 진행 상황과 커뮤니티가 참여할 수 있는 방법에 대해 공유하고자 합니다. 자세한 내용은 링크를 통해 확인할 수 있습니다.
👉 [자세히 보기](https://helm.sh/blog/path-to-helm-v4/)

