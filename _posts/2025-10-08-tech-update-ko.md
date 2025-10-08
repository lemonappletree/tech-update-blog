# 🛠️ 2025-10-08 기술 업데이트 요약

## 🔹 Kubernetes - Introducing Headlamp Plugin for Karpenter - Scaling and Visibility
이 기술 블로그 글은 Kubernetes의 오픈 소스 확장 가능 UI 프로젝트인 Headlamp와 Kubernetes의 노드 프로비저닝 프로젝트인 Karpenter의 새로운 플러그인에 대해 소개합니다. Headlamp Karpenter 플러그인은 실시간으로 Karpenter의 활동을 모니터링할 수 있는 기능을 제공합니다. 이를 통해 Karpenter의 리소스와 Kubernetes 객체 간의 관계를 확인하고, 실시간 메트릭을 시각화하며, 스케일링 이벤트를 추적할 수 있습니다. 이 플러그인은 LFX 멘토 프로젝트의 일환으로 개발되었습니다.

플러그인은 Karpenter의 리소스와 Kubernetes 리소스 간의 관계를 쉽게 확인할 수 있는 맵 뷰, 리소스 사용량 및 제한, 대기 중인 Pod, 프로비저닝 대기 시간 등의 메트릭을 시각화하는 기능을 제공하며, 스케일링 결정의 이유를 이해하고 디버깅하는 데 도움을 줍니다. 또한, Karpenter 구성 파일을 실시간으로 편집하고 검증할 수 있는 기능도 포함되어 있습니다.

Karpenter 플러그인은 AWS 및 Azure와 같은 일부 프로바이더에서 테스트되었으며, 사용자는 플러그인을 사용하여 피드백을 제공할 수 있습니다. 사용 방법 및 추가 정보는 GitHub의 플러그인 문서에서 확인할 수 있습니다.
👉 [자세히 보기](https://kubernetes.io/blog/2025/10/06/introducing-headlamp-plugin-for-karpenter/)

## 🔹 Spring Boot - Introducing Jackson 3 support in Spring
이 블로그 글은 Spring에서 Jackson 3 지원을 도입하는 내용을 다룹니다. Jackson은 JVM에서 가장 많이 사용되는 JSON 라이브러리로, Spring Boot 4와 관련 프로젝트에서 Jackson 3 지원을 통해 추가적인 개선을 제공하고자 합니다. Spring과 Jackson 팀 간의 긴밀한 협력으로 Jackson 3의 여러 개선 사항이 도입되었으며, Spring Boot 4는 Jackson 3 지원을 기본으로 하여 Jackson 2 지원을 점차 중단할 계획입니다. 이 글에서는 Jackson 3로의 마이그레이션 과정에서의 주요 변화와 주의할 점을 설명하고, Spring Data, Spring Security 등 Spring 생태계 전반에 걸친 Jackson 3 지원 상황을 다룹니다. Jackson 3는 보안, API, 기본 설정 등에서 강력한 이점을 제공하지만, 일부 변경 사항으로 인해 마이그레이션 작업이 필요할 수 있습니다. Spring 팀은 이 전환을 지원하기 위해 최선의 노력을 기울이고 있습니다.
👉 [자세히 보기](https://spring.io/blog/2025/10/07/introducing-jackson-3-support-in-spring)

## 🔹 Docker - Powered by Docker: How Open Source Genius Cut Entropy Debt with Docker MCP Toolkit and Claude Desktop
이 기술 블로그 글은 Docker의 활용 사례와 성공 스토리를 소개하는 "Powered by Docker" 시리즈의 일환으로, Docker 파트너 및 실무자의 경험을 다룹니다. 이 이야기는 라이언 워너(Ryan Wanner)에 의해 기고되었으며, 그는 15년 이상의 기업가 경험과 3년의 AI 소프트웨어 개발 경험을 가지고 있는 오픈 소스 창립자입니다. 글에서는 Docker MCP 툴킷과 Claude Desktop을 활용하여 엔트로피 부채를 줄인 사례가 소개됩니다.
👉 [자세히 보기](https://www.docker.com/blog/open-source-genius-cut-entropy-debt-docker-mcp-claude/)

## 🔹 Java - Java and AI: Powering Scalable, Enterprise-Grade Intelligence
이 블로그 글은 Oracle의 AI 이니셔티브와 솔루션이 Java에 대한 지속적인 투자와 함께 진행되고 있음을 설명합니다. AI는 산업을 변화시키고 새로운 수익 기회를 창출하며 고객 경험을 재정의하고 있습니다. 기업들이 실험 단계를 넘어 대규모 배포로 전환함에 따라 AI를 지원하는 기술 기반이 중요해지고 있으며, Java가 이러한 과정에서 중심적인 역할을 하고 있다고 강조합니다.
👉 [자세히 보기](https://inside.java/2025/10/07/java-and-ai-powering-enterprise-intelligence/)

## 🔹 Golang - Flight Recorder in Go 1.25
Go 1.25 버전에서는 새로운 진단 도구인 "플라이트 레코더"가 도입되었습니다. 이 도구는 프로그램 실행 중 발생하는 다양한 이벤트를 기록하여 성능 문제를 분석하고 디버깅하는 데 도움이 됩니다. 이를 통해 개발자는 보다 효율적으로 애플리케이션의 상태를 모니터링하고 문제를 해결할 수 있습니다.
👉 [자세히 보기](https://go.dev/blog/flight-recorder)

## 🔹 Helm - Path To Releasing Helm v4
제목: Helm v4 출시로 가는 길

요약: Helm v4의 첫 번째 알파 버전이 출시되었습니다. Helm v4 개발이 마지막 단계에 접어들면서, 현재 진행 상황과 더 넓은 커뮤니티가 어떻게 참여할 수 있는지에 대한 세부 사항을 공유하고자 합니다.
👉 [자세히 보기](https://helm.sh/blog/path-to-helm-v4/)

