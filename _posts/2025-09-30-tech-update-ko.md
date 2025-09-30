# 🛠️ 2025-09-30 기술 업데이트 요약

## 🔹 Kubernetes - Announcing Changed Block Tracking API support (alpha)
이 블로그 글은 Kubernetes에서 변경된 블록 추적(Changed Block Tracking) API의 알파 버전 지원을 발표하는 내용입니다. 이 기능은 CSI 스토리지 드라이버가 지속적으로 볼륨 스냅샷의 변경된 블록을 효율적으로 식별할 수 있도록 하여, 백업 작업을 더 빠르고 자원 효율적으로 수행할 수 있게 합니다. 변화된 블록 추적은 스냅샷 간의 블록 수준 변경을 추적하여 전체 볼륨을 스캔할 필요 없이 백업을 최적화합니다. 이는 Kubernetes의 컨테이너 스토리지 인터페이스(CSI)의 개선 사항으로, 대량의 데이터를 관리하는 Kubernetes 사용자에게 더욱 효율적인 백업 프로세스를 제공합니다. 현재 이 API는 블록 볼륨에만 지원되며 파일 기반 스토리지 시스템에는 적용되지 않습니다. 향후 피드백과 채택에 따라 베타 버전으로 발전할 계획입니다. Kubernetes Storage Special Interest Group(SIG)을 통해 프로젝트에 기여하거나 개발에 참여할 수 있습니다.
👉 [자세히 보기](https://kubernetes.io/blog/2025/09/25/csi-changed-block-tracking/)

## 🔹 Spring Boot - A Bootiful Podcast: Spring Batch lead Mahmoud Ben Hassine
블로그 글 요약: 이번 글에서는 Spring Batch 프로젝트의 전설적인 리더인 Mahmoud Ben Hassine과 함께 Spring Boot 4 세대에서의 최신 Spring Batch에 대해 이야기합니다.
👉 [자세히 보기](https://spring.io/blog/2025/09/25/a-bootiful-podcast-mahmoud-ben-hassine)

## 🔹 Docker - Expanding Docker Hardened Images: Secure Helm Charts for Deployments
블로그 글 요약: 소프트웨어 공급망 보안에 대한 요구가 증가하면서 개발팀은 신뢰할 수 있는 이미지, 간소화된 배포, 규정 준수 도구를 필요로 하고 있습니다. 고객들은 단기적인 공급업체가 아닌, 개발과 배포 전반에 걸쳐 신뢰할 수 있는 보안 파트너를 찾고 있습니다. 이러한 요구를 충족시키기 위해 Docker는 보안이 강화된 이미지와 Helm 차트를 제공하고 있습니다.
👉 [자세히 보기](https://www.docker.com/blog/docker-hardened-images-helm-charts-beta/)

## 🔹 Java - Episode 40 “Amber &amp; Valhalla - Incremental Design and Feature Arcs” with Brian Goetz
블로그 글 에피소드 40에서는 Nicolai Parlog이 Oracle의 Java 언어 설계자이자 Project Amber와 Project Valhalla의 리더인 Brian Goetz와 함께합니다. 이 에피소드에서는 Amber의 향후 기능 아크와 Valhalla의 null 제약 계획 등 두 프로젝트의 주요 업데이트와 통찰을 공유합니다.
👉 [자세히 보기](https://inside.java/2025/09/28/podcast-040/)

## 🔹 Golang - Flight Recorder in Go 1.25
Go 1.25 버전에서는 진단 도구에 새로운 기능인 '비행 기록(Flight Recorder)'이 도입되었습니다. 이 도구는 프로그램 실행 중 발생하는 다양한 이벤트를 기록하여 문제 진단과 성능 분석에 도움을 줍니다.
👉 [자세히 보기](https://go.dev/blog/flight-recorder)

## 🔹 Helm - Path To Releasing Helm v4
제목: Helm v4 출시 경로

요약: Helm v4의 첫 번째 알파 버전이 출시되었습니다. Helm v4 개발이 막바지에 이르렀으며, 현재 진행 상황과 더 넓은 커뮤니티가 참여할 수 있는 방법에 대한 세부 정보를 공유하고자 합니다.
👉 [자세히 보기](https://helm.sh/blog/path-to-helm-v4/)

