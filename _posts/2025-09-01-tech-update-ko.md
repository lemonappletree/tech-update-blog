# 🛠️ 2025-09-01 기술 업데이트 요약

## 🔹 Kubernetes - Kubernetes v1.34: Finer-Grained Control Over Container Restarts
이 블로그 글은 Kubernetes의 새로운 기능인 'Container Restart Policy and Rules'를 소개합니다. Kubernetes 1.34 버전에서는 Pod 내 각 컨테이너에 대해 개별적으로 재시작 정책을 설정할 수 있는 기능이 추가되었습니다. 이를 통해 Pod의 전체 재시작 정책을 무시하고 각 컨테이너의 종료 코드를 기반으로 조건부로 재시작할 수 있습니다. 이는 특히 AI/ML 훈련 작업과 같이 다양한 시나리오에서 유용합니다. 이 기능을 사용하려면 'ContainerRestartRules' 알파 기능 게이트를 활성화해야 합니다. 이 글에서는 이 기능의 사용 예제와 유용한 시나리오를 설명하며, Kubernetes 커뮤니티에 피드백을 요청하고 있습니다.
👉 [자세히 보기](https://kubernetes.io/blog/2025/08/29/kubernetes-v1-34-per-container-restart-policy/)

## 🔹 Spring Boot - A Bootiful Podcast: JobRunr founder Ronald Dehuysser on what's new in version 8
이번 기술 블로그 글에서는 SpringOne 2025 행사 직후, JobRunr 창립자 Ronald Dehuysser와 함께 JobRunr의 최신 버전 8.0.0에 대해 논의한 내용을 다루고 있습니다. 더 자세한 내용은 [JobRunr v8 블로그](https://www.jobrunr.io/en/blog/v8-release/)에서 확인할 수 있습니다.
👉 [자세히 보기](https://spring.io/blog/2025/08/28/a-bootiful-podcast-ronald-dehuysser)

## 🔹 Docker - Broadcom’s New Bitnami Restrictions? Migrate Easily with Docker
Broadcom의 새로운 Bitnami 제한으로 인해 Bitnami가 제공하던 인기 애플리케이션의 배포가 어려워질 수 있습니다. Bitnami는 오픈 소스 및 클라우드 네이티브 커뮤니티에서 중요한 역할을 해왔으며, 개발자들이 신뢰할 수 있는 컨테이너 이미지와 Helm 차트를 통해 애플리케이션을 쉽게 배포할 수 있도록 지원했습니다. 그러나 이러한 제약을 극복하고자 Docker를 사용하여 애플리케이션을 쉽게 마이그레이션할 수 있는 방법을 소개합니다.
👉 [자세히 보기](https://www.docker.com/blog/broadcoms-new-bitnami-restrictions-migrate-easily-with-docker/)

## 🔹 Java - All New Java Language Features Since Java 21 #RoadTo25
블로그 글 요약: "Java 25는 데이터 지향 프로그래밍, 신규 개발자 지원, 스크립팅 언어로서 Java의 활용성을 높이기 위한 다양한 새로운 언어 기능을 제공합니다. 이 글에서는 Jose가 이러한 새로운 기능들을 탐구합니다."
👉 [자세히 보기](https://inside.java/2025/08/31/roadto25-java-language/)

## 🔹 Golang - Testing Time (and other asynchronicities)
블로그 글 "Testing Time (and other asynchronicities)"는 비동기 코드 테스트 방법과 `testing/synctest` 패키지에 대한 내용을 다룹니다. 이는 GopherCon Europe 2025에서 같은 제목으로 발표된 내용을 바탕으로 작성되었습니다. 이 글에서는 비동기 코드의 테스트에서 발생할 수 있는 문제와 이를 효율적으로 해결하기 위한 접근법을 설명합니다.
👉 [자세히 보기](https://go.dev/blog/testing-time)

## 🔹 Helm - Helm @ KubeCon + CloudNativeCon EU '25
블로그 글 요약: Helm 팀이 4월 1일부터 4일까지 영국 런던에서 열리는 KubeCon + CloudNativeCon EU '25에 참가합니다. Helm 4의 출시가 예정되어 있어, 이번 행사에서 유지 관리자들과의 대화에 참여하고, Helm 부스에서 다양한 정보를 얻을 수 있습니다. 행사 기간 동안 진행될 Helm 관련 활동들에 대한 자세한 내용은 블로그에서 확인할 수 있습니다.
👉 [자세히 보기](https://helm.sh/blog/helm-at-kubecon-eu-25/)

