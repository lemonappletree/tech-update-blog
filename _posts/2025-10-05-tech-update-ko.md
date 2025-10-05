# 🛠️ 2025-10-05 기술 업데이트 요약

## 🔹 Kubernetes - Announcing Changed Block Tracking API support (alpha)
이 기술 블로그 글은 Kubernetes가 "변경된 블록 추적" 기능을 알파 지원으로 도입했음을 발표한 내용입니다. 이 기능은 CSI 스토리지 드라이버가 영구 볼륨 스냅샷에서 변경된 블록을 식별할 수 있도록 하여, 백업 작업을 더욱 빠르고 자원 효율적으로 수행할 수 있게 합니다. 이 API는 스냅샷 간의 블록 수준 변경을 추적하여 전체 볼륨을 스캔할 필요를 없애며, Kubernetes의 상태 저장 워크로드에 효율적인 백업 솔루션을 제공합니다. 현재는 블록 볼륨에만 지원되며, 파일 볼륨은 지원되지 않습니다. 이 기능을 통해 백업 프로세스가 더 효율적이 되고, 백업 시간 및 자원 소비를 줄일 수 있습니다. 개발자들은 이 기능을 활용하기 위해 CSI 드라이버와 외부 스냅샷 메타데이터 사이드카를 구현해야 합니다.
👉 [자세히 보기](https://kubernetes.io/blog/2025/09/25/csi-changed-block-tracking/)

## 🔹 Spring Boot - Spring Cloud 2025.1.0-M3 (aka Oakwood) has been released
Spring Cloud 2025.1.0-M3(Oakwood) 릴리스가 발표되었습니다. 이번 릴리스는 Spring Boot 4.0.0-M3에 의존하며, 주요 변경 사항으로는 Spring Cloud Function에서 spring-cloud-function-rscoket과 spring-cloud-function-deployer가 중단되었고, Spring Cloud Kubernetes에서는 Kubernetes Java Client와 Fabric8 Kubernetes Client가 각각 24.0.0과 7.4.0으로 업그레이드되었습니다. 또한, Spring Cloud Contract에서는 stubrunner 속성이 spring.cloud.contract.stubrunner로 변경되었고, Spring Cloud Circuitbreaker는 Resilience4j를 2.3.0으로 업그레이드했습니다. 이 외에도 다양한 모듈들이 업데이트되었습니다. 자세한 사항은 릴리스 노트를 참조하고, 피드백은 GitHub, Gitter, Stack Overflow, Twitter를 통해 받을 수 있습니다. Maven과 Gradle을 사용한 의존성 관리 방법도 제공됩니다.
👉 [자세히 보기](https://spring.io/blog/2025/10/03/spring-cloud-2025-1-0-M3-aka-oakwood-has-been-released)

## 🔹 Docker - From Shell Scripts to Science Agents: How AI Agents Are Transforming Research Workflows
이 블로그 글은 인공지능 에이전트가 연구 워크플로우를 어떻게 혁신하고 있는지를 다룹니다. 예전에는 연구자들이 쉘 스크립트와 엑셀 시트를 사용해 복잡한 작업을 관리했지만, 이제 AI 에이전트가 이러한 반복적이고 시간이 많이 드는 작업을 자동화하여 연구자들이 더 창의적이고 가치 있는 활동에 집중할 수 있게 도와줍니다. AI 에이전트는 데이터 분석, 문헌 검색 및 실험 모델 실행을 보다 효율적으로 수행하게 해 줍니다.
👉 [자세히 보기](https://www.docker.com/blog/ai-science-agents-research-workflows/)

## 🔹 Java - The Inside Java Newsletter: Java 25 is Live!
제목: The Inside Java Newsletter: Java 25가 출시되었습니다!

요약: 2025년 9월자 Inside Java 뉴스레터는 Java 25에 관한 기술 비디오 시리즈에 중점을 두고 있습니다. 또한 Java 사용자 그룹, 개발자 이벤트, 학습 자료, 커뮤니티 팟캐스트, 그리고 Java 플랫폼 그룹의 콘텐츠에 대한 업데이트를 제공합니다. 개발자, 학습자, 교육자 및 고객을 위한 멀티미디어 콘텐츠는 learn.java, dev.java, inside.java에서 확인할 수 있습니다. 아카이브를 보고 구독하며 친구에게 공유할 수 있습니다.
👉 [자세히 보기](https://inside.java/2025/10/03/inside-java-newsletter/)

## 🔹 Golang - Flight Recorder in Go 1.25
제목: Go 1.25의 비행 기록 장치
요약: Go 1.25 버전에서는 진단 도구 모음에 새로운 도구인 비행 기록 기능이 도입되었습니다. 이 기능은 프로그램 실행 중 발생하는 다양한 이벤트를 기록하고 분석하는 데 도움이 됩니다. 더 자세한 내용은 [링크](https://go.dev/blog/flight-recorder)에서 확인할 수 있습니다.
👉 [자세히 보기](https://go.dev/blog/flight-recorder)

## 🔹 Helm - Path To Releasing Helm v4
제목: Helm v4 출시를 향한 여정

요약: Helm v4의 첫 번째 알파 버전이 출시되었습니다. Helm v4 개발이 막바지에 이르렀으므로, 현재 진행 상황과 커뮤니티가 어떻게 참여할 수 있는지에 대한 세부 정보를 공유하고자 합니다.
👉 [자세히 보기](https://helm.sh/blog/path-to-helm-v4/)

