# 🛠️ 2025-10-09 기술 업데이트 요약

## 🔹 Kubernetes - Introducing Headlamp Plugin for Karpenter - Scaling and Visibility
이 블로그 글은 Kubernetes의 클러스터 관리 도구인 Headlamp와 자동 스케일링 도구인 Karpenter의 통합을 소개합니다. Headlamp는 오픈소스 Kubernetes UI 프로젝트로, 클러스터 자원을 탐색하고 관리하는 데 사용됩니다. Karpenter는 빠르고 효율적인 클러스터 스케일링을 지원하는 자동 노드 프로비저닝 도구입니다.

새로 출시된 Headlamp의 Karpenter 플러그인은 Headlamp UI에서 Karpenter의 활동을 실시간으로 시각화할 수 있도록 도와줍니다. 이 플러그인을 통해 Kubernetes 객체와 Karpenter 자원의 관계를 확인하고, 실시간 메트릭 및 스케일링 이벤트를 모니터링할 수 있습니다. 사용자는 프로비저닝 중인 대기 중인 파드를 검사하고, 스케일링 결정을 검토하며, Karpenter 관리 자원을 편집할 수 있습니다.

이 플러그인은 Kubernetes 사용자와 운영자가 클러스터의 자동 스케일링 동작을 이해하고 디버깅하며 최적화하는 데 도움을 줍니다. 플러그인은 다양한 Karpenter 공급자와 호환되며, 현재 AWS와 Azure에서 테스트되었습니다. 사용법에 대한 자세한 내용은 GitHub의 README.md 파일을 참조하라고 안내합니다.
👉 [자세히 보기](https://kubernetes.io/blog/2025/10/06/introducing-headlamp-plugin-for-karpenter/)

## 🔹 Spring Boot - Introducing Jackson 3 support in Spring
이 블로그 글은 Spring에서 Jackson 3 지원을 소개하는 내용입니다. 최근 Jackson 3.0.0이 정식 출시됨에 따라 Spring Boot 4와 관련 프로젝트에서 새로운 Jackson 3 지원을 도입할 예정입니다. Jackson은 JVM에서 가장 많이 사용되는 JSON 라이브러리 중 하나로, 이번 지원 도입을 통해 여러 개선 사항들이 추가됩니다. Spring 팀은 Jackson 팀과 긴밀히 협력하여 Jackson 3의 다양한 기능을 활용할 수 있도록 피드백을 반영하고, Spring과 Jackson의 기본 설정을 맞추는 등의 작업을 진행했습니다.

Spring Boot 4에서는 Jackson 3를 기본으로 지원하며, Jackson 2에 대한 지원은 점차 중단될 예정입니다. 하지만 Jackson 2와 3을 동시에 사용할 수도 있으며, 이전 버전의 데이터 마이그레이션을 돕기 위한 호환 모드도 제공됩니다. Jackson 3로의 마이그레이션 과정에서는 패키지 업데이트, 기본 설정 변경, 모듈 자동 탐색 기능 등을 고려해야 합니다. 또한, Spring Security와 Spring Data에서도 Jackson 3 지원이 추가되었으며, 일부 모듈은 Jackson 2를 계속 사용할 수 있습니다.

이 글은 Jackson 3의 도입이 보안, API, 기본 설정 및 기능 면에서 많은 이점을 제공하지만, 몇 가지 마이그레이션 작업이 필요함을 강조합니다. Spring 팀은 사용자의 피드백을 바탕으로 가이드를 개선하고 문서화를 통해 관련 질문에 답변할 예정입니다.
👉 [자세히 보기](https://spring.io/blog/2025/10/07/introducing-jackson-3-support-in-spring)

## 🔹 Docker - From the Captain’s Chair: Pradumna Saraf
블로그 글 "From the Captain’s Chair: Pradumna Saraf"는 Docker 커뮤니티의 리더이자 전문가인 Docker Captains에 대해 다루는 시리즈 중 하나입니다. 이 시리즈는 각 Captain의 경험과 개인적인 이야기를 통해 그들을 더 깊이 이해할 수 있는 기회를 제공합니다. 이번 글에서는 Pradumna Saraf를 인터뷰하여 그의 경험과 Docker에 대한 열정을 공유합니다.
👉 [자세히 보기](https://www.docker.com/blog/from-the-captains-chair-pradumna-saraf/)

## 🔹 Java - Unlock Powerful Insights with Java Management Service: Introducing Analyze Applications and Major Management Enhancements
Oracle Java Management Service(JMS)의 새로운 기능을 소개하는 기술 블로그 글입니다. 이번 업데이트에서는 Analyze Applications라는 혁신적인 기능이 도입되었으며, 현대적인 Java 환경 관리에 필수적인 주요 개선사항들이 추가되었습니다. 이 개선사항에는 향상된 작업 스케줄링, Kubernetes에서의 Java 워크로드 지원 확장, Oracle의 Enterprise Performance Pack과의 통합 등이 포함되어 있습니다. 이를 통해 Java 관리 서비스의 강력한 인사이트를 제공하고 Java 환경의 효율적인 관리를 지원합니다.
👉 [자세히 보기](https://inside.java/2025/10/08/jms-analyze-applications/)

## 🔹 Golang - Flight Recorder in Go 1.25
Go 1.25 버전에서는 진단 도구 상자에 새로운 도구인 '비행 기록'이 추가되었습니다. 이 도구는 프로그램 실행 중 발생하는 다양한 이벤트와 데이터를 기록하여 문제를 분석하고 디버깅하는 데 도움을 줍니다.
👉 [자세히 보기](https://go.dev/blog/flight-recorder)

## 🔹 Helm - Path To Releasing Helm v4
제목: Helm v4 출시를 위한 여정

요약: Helm v4의 첫 번째 알파 버전이 출시되었습니다. Helm v4 개발이 막바지에 이르렀으며, 현재 진행 상황과 더 넓은 커뮤니티가 어떻게 참여할 수 있는지에 대한 세부 정보를 공유하고자 합니다.
👉 [자세히 보기](https://helm.sh/blog/path-to-helm-v4/)

