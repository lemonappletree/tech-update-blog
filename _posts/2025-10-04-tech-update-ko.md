# 🛠️ 2025-10-04 기술 업데이트 요약

## 🔹 Kubernetes - Announcing Changed Block Tracking API support (alpha)
이 기술 블로그 글은 Kubernetes의 스토리지 에코시스템을 위한 변경된 블록 추적(Changed Block Tracking) API의 알파 지원을 발표합니다. 이 기능은 CSI(Storage Container Interface) 스토리지 드라이버가 영구 볼륨 스냅샷에서 변경된 블록을 식별할 수 있도록 하여 백업 작업을 더 빠르고 자원 효율적으로 수행할 수 있게 합니다. 변경된 블록 추적은 블록 수준에서 스냅샷 간의 변경 사항을 추적하여 볼륨 전체를 스캔할 필요성을 없애주며, 이는 백업 프로세스를 크게 개선합니다. 이 기능은 현재 블록 볼륨에만 지원되며 파일 볼륨은 지원되지 않습니다. Kubernetes 사용자는 이 API를 통해 더욱 효율적인 백업을 수행할 수 있으며, 이는 백업 시간 단축과 자원 소모 감소에 기여합니다. 이 글은 또한 구현 요구 사항 및 시작 방법에 대해 설명하며, 커뮤니티 참여를 권장합니다.
👉 [자세히 보기](https://kubernetes.io/blog/2025/09/25/csi-changed-block-tracking/)

## 🔹 Spring Boot - Spring Cloud 2025.1.0-M3 (aka Oakwood) has been released
Spring Cloud 커뮤니티는 Spring Cloud 2025.1.0 릴리스 트레인의 마일스톤 3(M3) 버전이 출시되었음을 발표했습니다. 이번 릴리스는 Spring Milestone 저장소에서 확인할 수 있으며, 주요 변경 사항으로는 Spring Cloud Function에서 일부 기능이 중단되었고, Spring Cloud Kubernetes와 Spring Cloud Circuitbreaker에서 클라이언트 버전이 업그레이드되었습니다. 또한 Spring Cloud Contract와 Spring Cloud Commons에서도 몇 가지 중요한 업데이트가 이루어졌습니다. 각 모듈의 버전은 2025.1.0-M3로 업데이트되었으며, 자세한 내용은 GitHub 릴리스 노트를 참고할 수 있습니다. 사용자 피드백은 GitHub, Gitter, Stack Overflow 또는 Twitter를 통해 받습니다. Maven과 Gradle을 통한 시작 방법도 포함되어 있습니다.
👉 [자세히 보기](https://spring.io/blog/2025/10/03/spring-cloud-2025-1-0-M3-aka-oakwood-has-been-released)

## 🔹 Docker - From Shell Scripts to Science Agents: How AI Agents Are Transforming Research Workflows
블로그 글은 AI 에이전트가 연구 워크플로우를 어떻게 변화시키고 있는지를 다룹니다. 과거에는 연구자들이 여러 개의 터미널을 열어두고, 셸 스크립트를 이용해 단백질 접힘 모델을 실행하고, CSV 파일을 분석하며, 관련 문헌을 검색하는 등의 작업을 수작업으로 처리해야 했습니다. 그러나 AI 에이전트의 도입으로 이러한 복잡한 작업들이 자동화되어 연구자들이 더 효율적으로 연구를 진행할 수 있게 되었습니다. AI 에이전트는 데이터 처리, 분석, 문헌 검색 등 다양한 분야에서 연구자들을 지원하며, 연구의 효율성과 정확성을 높이고 있습니다.
👉 [자세히 보기](https://www.docker.com/blog/ai-science-agents-research-workflows/)

## 🔹 Java - The Inside Java Newsletter: Java 25 is Live!
기술 블로그 글의 요약: 2025년 9월의 Inside Java 뉴스레터는 Java 25에 대한 기술 비디오 시리즈에 중점을 두고 있습니다. 또한 Java 사용자 그룹, 개발자 이벤트, 학습 자료, 커뮤니티 팟캐스트 및 Java 플랫폼 그룹의 콘텐츠에 대한 업데이트도 포함되어 있습니다. 개발자, 학습자, 교육자, 고객을 위한 멀티미디어 콘텐츠는 learn.java, dev.java, inside.java에서 확인할 수 있습니다. 아카이브를 보고, 구독하고, 친구에게 공유할 수 있습니다.
👉 [자세히 보기](https://inside.java/2025/10/03/inside-java-newsletter/)

## 🔹 Golang - Flight Recorder in Go 1.25
Go 1.25 버전에서는 새로운 진단 도구인 '비행 기록' 기능을 도입했습니다. 이 기능은 프로그램의 실행 상태를 기록하고 분석하는 데 도움을 줍니다.
👉 [자세히 보기](https://go.dev/blog/flight-recorder)

## 🔹 Helm - Path To Releasing Helm v4
제목: Helm v4 출시를 향한 여정

요약: Helm v4의 첫 번째 알파 버전이 출시되었습니다. Helm v4 개발이 마무리 단계에 접어든 만큼, 현재 진행 상황과 더 넓은 커뮤니티가 어떻게 참여할 수 있는지에 대한 세부 사항을 공유하고자 합니다.
👉 [자세히 보기](https://helm.sh/blog/path-to-helm-v4/)

