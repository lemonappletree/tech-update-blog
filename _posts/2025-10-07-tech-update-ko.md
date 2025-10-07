# 🛠️ 2025-10-07 기술 업데이트 요약

## 🔹 Kubernetes - Introducing Headlamp Plugin for Karpenter - Scaling and Visibility
이 블로그 글은 Karpenter를 위한 Headlamp 플러그인의 도입을 소개합니다. Headlamp는 오픈 소스 Kubernetes UI 프로젝트로 클러스터 자원을 탐색, 관리, 디버깅할 수 있게 해줍니다. Karpenter는 Kubernetes의 자동 스케일링 프로젝트로, 클러스터의 빠르고 효율적인 확장을 돕습니다. 새로운 Headlamp Karpenter 플러그인은 Karpenter의 활동을 실시간으로 볼 수 있게 하며, Kubernetes 객체와의 관계, 라이브 메트릭, 스케일링 이벤트 등을 보여줍니다. 이 플러그인은 LFX 멘토 프로젝트의 일환으로 제작되었습니다. 플러그인은 Karpenter 리소스와 Kubernetes 리소스 간의 관계를 시각화하고, 리소스 사용과 제한, 대기 중인 Pod, 프로비저닝 지연 등을 즉시 파악할 수 있게 해줍니다. 확장 결정과 구성 편집 기능도 제공하며, 실시간으로 Karpenter 리소스를 추적할 수 있습니다. 플러그인은 AWS, Azure 등의 프로바이더에서 테스트되었으며, 다른 프로바이더에 대한 지원도 받을 수 있습니다. 사용 방법은 GitHub의 플러그인 페이지를 참고하세요.
👉 [자세히 보기](https://kubernetes.io/blog/2025/10/06/introducing-headlamp-plugin-for-karpenter/)

## 🔹 Spring Boot - Spring AI 1.1.0-M3 Available Now
Spring AI 1.1.0-M3 버전이 출시되었습니다. 이번 릴리스는 주로 Model Context Protocol (MCP) 개선에 중점을 두고 있으며, MCP Java SDK v0.14.0 업그레이드와 리소스 템플릿 기능, 보안 문서가 포함되어 있습니다. 주요 개선 사항으로는 MCP 통합 강화, Azure Cosmos DB 챗 메모리 추가, 안정성 향상, 문서 개선, 종속성 업그레이드 등이 있습니다. 또한, 다양한 기능 영역에서 향상된 기능들이 도입되었습니다. 개발자들은 향상된 도구 통합 워크플로우를 경험할 수 있으며, 향후 출시될 Spring AI 1.1 GA 버전을 위해 MCP 개선, 챗 모델 기능 확장, 챗 메모리 문제 해결 등에 집중할 예정입니다.
👉 [자세히 보기](https://spring.io/blog/2025/10/06/spring-ai-1-1-0-M3-available-now)

## 🔹 Docker - IBM Granite 4.0 Models Now Available on Docker Hub
요약: 개발자들은 이제 Docker Hub 모델 카탈로그에서 IBM의 최신 오픈 소스 Granite 4.0 언어 모델을 발견하고 실행할 수 있으며, Docker Model Runner를 사용하여 몇 분 만에 개발을 시작할 수 있습니다. Granite 4.0은 강력하고 기업에 적합한 성능과 가벼운 구조를 결합하여 로컬에서 프로토타입을 만들고 자신 있게 확장할 수 있도록 설계되었습니다. Granite 4.0 모델은 속도와 유연성을 중시하여 설계되었습니다.
👉 [자세히 보기](https://www.docker.com/blog/ibm-granite-4-0-models-now-available-on-docker-hub/)

## 🔹 Java - Evolving ZGC’s Pointer Color Palette #JVMLS
이 기술 블로그 글은 ZGC의 포인터 색상 사용에 대한 내용을 다룹니다. ZGC에서 포인터에 색상을 입히는 것은 알고리즘의 핵심 요소 중 하나이며, 적절한 색상을 선택하는 것이 매우 중요합니다. ZGC의 복잡성이 증가함에 따라 색상 팔레트도 진화하여 더 세밀한 표현이 가능해졌습니다. 이 프레젠테이션에서는 비세대형 ZGC에서 세대형 ZGC로의 변화와 함께, 향후 ZGC의 진화 단계인 스레드 로컬 가비지 컬렉션(thread-local GC)을 준비하는 과정에서의 색상 선택 변화에 대해 설명합니다.
👉 [자세히 보기](https://inside.java/2025/10/06/jvmls-zgc-colored-pointers/)

## 🔹 Golang - Flight Recorder in Go 1.25
Go 1.25에서 새로운 진단 도구인 '비행 기록' 기능이 도입되었습니다. 이 기능은 프로그램 실행 중 발생하는 다양한 이벤트를 기록하여 문제를 진단하고 성능을 분석하는 데 유용합니다.
👉 [자세히 보기](https://go.dev/blog/flight-recorder)

## 🔹 Helm - Path To Releasing Helm v4
Helm v4의 첫 번째 알파 버전이 출시되었습니다. Helm v4 개발이 막바지에 이르렀으며, 이번 블로그 글에서는 현재 진행 상황과 더 넓은 커뮤니티가 어떻게 참여할 수 있는지를 공유하고자 합니다.
👉 [자세히 보기](https://helm.sh/blog/path-to-helm-v4/)

