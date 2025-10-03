# 🛠️ 2025-10-03 기술 업데이트 요약

## 🔹 Kubernetes - Announcing Changed Block Tracking API support (alpha)
이 기술 블로그 글은 Kubernetes의 저장소 생태계를 개선하기 위한 변경 블록 추적(Changed Block Tracking) API의 알파 지원 발표에 관한 내용입니다. 이 새로운 기능은 CSI 저장소 드라이버가 영구 볼륨 스냅샷에서 변경된 블록을 식별할 수 있게 하여 백업 작업을 더 빠르고 자원 효율적으로 수행할 수 있도록 합니다. 이 API는 전체 볼륨을 스캔하지 않고도 스냅샷 간의 블록 수준 변경을 추적할 수 있게 해주어 대규모 데이터셋을 관리하는 Kubernetes 사용자에게 백업 프로세스를 더욱 효율적으로 만들어 줍니다.

현재 이 API는 블록 볼륨에만 지원되며, 파일 볼륨에는 지원되지 않습니다. Kubernetes에서의 변경 블록 추적의 장점으로는 긴 백업 시간, 높은 자원 사용량, 증가하는 저장 비용 문제를 해결할 수 있다는 것입니다. 이를 통해 증분 백업 기능을 제공하며, 백업 솔루션은 변경된 블록만을 처리하는 방식으로 백업 효율성을 높일 수 있습니다. 

이 기능을 구현하기 위해서는 CSI 드라이버, 외부 스냅샷 메타데이터 사이드카 등의 구성요소가 필요하며, 스토리지 제공자는 특정 CSI RPC를 구현해야 합니다. 백업 솔루션은 인증 설정, 스트리밍 클라이언트 측 코드 구현 등을 통해 이 기능을 활용할 수 있습니다. 향후 피드백과 채택에 따라 이 기능은 베타 단계로 발전할 계획입니다. Kubernetes Storage Special Interest Group(SIG)에서는 새로운 기여자를 환영하고 있습니다.
👉 [자세히 보기](https://kubernetes.io/blog/2025/09/25/csi-changed-block-tracking/)

## 🔹 Spring Boot - A Bootiful Podcast: Dr. Kris De Volder on developer tooling for Spring developers and AI
이 블로그 글은 Spring 개발자들을 위한 도구와 AI에 대해 이야기하는 팟캐스트 에피소드를 다루고 있습니다. 이번 회차에서는 Spring 도구의 전설인 Dr. Kris De Volder가 출연하여 도구, AI 등 다양한 주제에 대해 논의합니다.
👉 [자세히 보기](https://spring.io/blog/2025/10/02/a-bootiful-podcast-dr-kris-de-volder)

## 🔹 Docker - From Shell Scripts to Science Agents: How AI Agents Are Transforming Research Workflows
이 기술 블로그 글은 AI 에이전트가 연구 워크플로우를 어떻게 변화시키고 있는지를 설명합니다. 전통적으로 연구자들은 쉘 스크립트와 여러 도구를 사용하여 복잡한 과정을 관리해야 했습니다. 하지만 AI 에이전트의 등장으로 인해, 이러한 반복적이고 시간이 많이 소요되는 작업들이 자동화되고, 연구자들은 더 창의적이고 중요한 작업에 집중할 수 있게 되었습니다. 이 글은 AI 기술이 실험 데이터 처리, 문헌 검색, 모델 실행 등을 어떻게 효율화하는지를 다루고 있습니다.
👉 [자세히 보기](https://www.docker.com/blog/ai-science-agents-research-workflows/)

## 🔹 Java - Oracle Java Extension for Visual Studio Code Version 24.1.2 Is Now Available!
제목: Oracle Java Extension for Visual Studio Code 버전 24.1.2 출시!

요약: Visual Studio Code를 위한 새로운 Java 플랫폼 확장판이 출시되었습니다. 최신 업데이트를 통해 개발 환경에서 Java를 더욱 쉽게 사용할 수 있게 되었습니다. 자세한 내용은 링크를 통해 확인할 수 있습니다.
👉 [자세히 보기](https://inside.java/2025/10/01/java-vscode-extension-update/)

## 🔹 Golang - Flight Recorder in Go 1.25
Go 1.25 버전에서는 진단 도구 모음에 새로운 도구인 "플라이트 레코더"가 도입되었습니다. 이 도구는 프로그램 실행 중 발생하는 다양한 이벤트를 기록하여 문제를 진단하고 성능을 분석하는 데 도움을 줍니다.
👉 [자세히 보기](https://go.dev/blog/flight-recorder)

## 🔹 Helm - Path To Releasing Helm v4
제목: Helm v4 출시 경로

요약: Helm v4의 첫 번째 알파 버전이 출시되었습니다. Helm v4 개발이 막바지에 이르렀기 때문에, 현재 진행 상황과 더 넓은 커뮤니티가 어떻게 참여할 수 있는지에 대한 세부 사항을 공유하고자 합니다. 더 자세한 내용은 [블로그 링크](https://helm.sh/blog/path-to-helm-v4/)를 참조하세요.
👉 [자세히 보기](https://helm.sh/blog/path-to-helm-v4/)

