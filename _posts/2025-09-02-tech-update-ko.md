# 🛠️ 2025-09-02 기술 업데이트 요약

## 🔹 Kubernetes - Kubernetes v1.34: DRA has graduated to GA
Kubernetes 1.34 버전이 발표되었으며, Dynamic Resource Allocation(DRA)의 주요 개선 사항이 포함되었습니다. 이번 릴리스에서 `resource.k8s.io` 그룹의 여러 API가 안정화 단계인 GA(General Availability)로 승격되어, Kubernetes에서 장치 관리의 잠재력을 극대화할 수 있게 되었습니다. 또한, 몇 가지 주요 기능이 베타로 이동하였으며, 새로운 알파 기능들이 추가되어 더 많은 표현력과 유연성을 제공합니다.

DRA는 특수 하드웨어 및 인프라 자원 관리에 유연한 프레임워크를 제공하며, 이번 GA 승격으로 안정성을 확보하고 장기적으로 Kubernetes의 일부분이 되었습니다. Kubernetes 1.34부터 DRA는 기본적으로 활성화되며, 베타 단계에 도달한 DRA 기능들도 기본적으로 활성화됩니다.

베타로 승격된 기능으로는 관리자가 특정 사용자에게 디바이스 지원을 제한할 수 있는 "Admin access labelling"과, 하나의 고성능 GPU 외에도 여러 중간 수준 GPU를 사용할 수 있도록 하는 "Prioritized list"가 있습니다. 새로운 알파 기능으로는 "Extended resource mapping", "Consumable capacity", "Binding conditions", 그리고 "Resource health status"가 포함되어, 향후 리소스 관리의 향상된 방향성을 보여줍니다.

향후 릴리스에서는 DRA의 성능, 확장성 및 신뢰성을 지속적으로 개선할 예정이며, 다양한 단계의 기능들이 GA로 이동될 계획입니다. DRA 개선에 관심이 있다면 WG Device Management Slack 채널에 참여하여 기여할 수 있습니다.
👉 [자세히 보기](https://kubernetes.io/blog/2025/09/01/kubernetes-v1-34-dra-updates/)

## 🔹 Spring Boot - A Bootiful Podcast: JobRunr founder Ronald Dehuysser on what's new in version 8
제목: 아름다운 팟캐스트: JobRunr 창립자 Ronald Dehuysser가 설명하는 버전 8의 새로운 기능

요약: Spring 팬 여러분, 안녕하세요! 이번 에피소드에서는 2025년 SpringOne 행사를 방금 마친 후, JobRunr의 창립자 Ronald Dehuysser와 함께 버전 8.0.0의 새로운 기능에 대해 이야기할 수 있어 기뻤습니다. JobRunr v8에 대한 자세한 내용은 [여기](https://www.jobrunr.io/en/blog/v8-release/)에서 확인하세요!
👉 [자세히 보기](https://spring.io/blog/2025/08/28/a-bootiful-podcast-ronald-dehuysser)

## 🔹 Docker - Broadcom’s New Bitnami Restrictions? Migrate Easily with Docker
블로그 글은 Broadcom의 새로운 Bitnami 사용 제한에 대한 내용을 다루고 있습니다. Bitnami는 오픈 소스 및 클라우드 네이티브 커뮤니티에서 중요한 역할을 해왔으며, 개발자와 운영자가 인기 있는 애플리케이션을 신뢰성 있는 사전 구축된 컨테이너 이미지와 Helm 차트를 사용하여 쉽게 배포할 수 있도록 지원해왔습니다. 이로 인해 WordPress부터 PostgreSQL까지 다양한 팀이 설치 및 업데이트를 표준화하는 데 도움을 받았습니다. 글은 이러한 Bitnami의 제약을 극복하기 위해 Docker를 사용하여 쉽게 마이그레이션하는 방법을 소개합니다.
👉 [자세히 보기](https://www.docker.com/blog/broadcoms-new-bitnami-restrictions-migrate-easily-with-docker/)

## 🔹 Java - All New Java Language Features Since Java 21 #RoadTo25
기술 블로그 글 요약: "Java 25는 데이터 중심 프로그래밍, 신규 개발자 지원, 스크립팅 언어로서의 Java의 활용성을 높이는 여러 새로운 언어 기능을 제공합니다. Jose와 함께 이러한 기능들을 탐구해보세요."
👉 [자세히 보기](https://inside.java/2025/08/31/roadto25-java-language/)

## 🔹 Golang - Testing Time (and other asynchronicities)
블로그 글 "Testing Time (and other asynchronicities)"는 비동기 코드를 테스트하는 방법에 대해 논의하며, `testing/synctest` 패키지를 탐구합니다. 이 글은 GopherCon Europe 2025에서 발표된 동일한 제목의 강연을 바탕으로 작성되었습니다.
👉 [자세히 보기](https://go.dev/blog/testing-time)

## 🔹 Helm - Helm @ KubeCon + CloudNativeCon EU '25
이번 주 4월 1일부터 4일까지 영국 런던에서 열리는 KubeCon + CloudNativeCon EU '25에 Helm 팀이 참가합니다. 올해 말 출시 예정인 Helm 4에 대한 논의가 진행될 예정이니, 발표 세션과 Project Pavilion의 Helm 부스를 방문하여 유지보수자들과 대화를 나누어 보세요. 한 주 동안 진행될 모든 Helm 관련 활동에 대한 자세한 내용은 블로그에서 확인할 수 있습니다.
👉 [자세히 보기](https://helm.sh/blog/helm-at-kubecon-eu-25/)

