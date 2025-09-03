# 🛠️ 2025-09-03 기술 업데이트 요약

## 🔹 Kubernetes - Kubernetes v1.34: Introducing CPU Manager Static Policy Option for Uncore Cache Alignment
이 기술 블로그 글에서는 Kubernetes v1.34에서 도입된 CPU Manager Static Policy 옵션인 `prefer-align-cpus-by-uncorecache`에 대해 설명합니다. 이 옵션은 분할된 Uncore Cache 구조를 가진 프로세서에서 특정 워크로드의 성능을 최적화하기 위해 설계되었습니다. Uncore Cache는 CPU 코어와 직접 연결되지 않은 마지막 레벨의 캐시입니다. 최근 AMD64와 ARM 아키텍처 기반 프로세서들은 접근 지연 시간을 줄이기 위해 마지막 레벨의 캐시를 여러 물리적 캐시로 나누는 분할된 Uncore Cache 구조를 도입했습니다. 이 옵션을 사용하면 Kubernetes가 컨테이너에 할당되는 CPU 리소스가 동일한 Uncore Cache를 공유하도록 하여 캐시 지연 시간을 줄이고, 컨테이너 간의 캐시 경쟁을 최소화할 수 있습니다. 이 기능은 vRAN, 모바일 패킷 코어, 방화벽 같은 텔레콤 애플리케이션에 유용할 수 있으며, Kubernetes의 kubelet 설정 파일을 수정하여 활성화할 수 있습니다.
👉 [자세히 보기](https://kubernetes.io/blog/2025/09/02/kubernetes-v1-34-prefer-align-by-uncore-cache-cpumanager-static-policy-optimization/)

## 🔹 Spring Boot - The Road to GA - Introduction
이 기술 블로그 글은 스프링(Spring) 포트폴리오가 올해 11월에 출시될 예정인 주요 버전 업데이트를 준비하고 있다는 내용을 소개합니다. 스프링 부트의 네 번째 주요 세대와 스프링 프레임워크의 일곱 번째 주요 세대가 될 예정이며, JDK 17을 유지하면서도 Jakarta EE 11, Kotlin 2, Jackson 3, JUnit 6 등 여러 업그레이드를 포함할 계획입니다. 11월까지 매주 새로운 기능에 대한 블로그 글을 게시할 예정이며, 이에 대한 일정과 주제를 표로 정리했습니다. 커뮤니티의 피드백을 바탕으로 많은 기능이 추가되었으며, Maven Central에서 이미 일부 새로운 기능을 경험할 수 있습니다. 독자들은 새로운 블로그 글을 계속 확인할 수 있도록 이 페이지를 즐겨찾기 하기를 권장합니다.
👉 [자세히 보기](https://spring.io/blog/2025/09/02/road_to_ga_introduction)

## 🔹 Docker - Broadcom’s New Bitnami Restrictions? Migrate Easily with Docker
블로그 글은 Broadcom의 새로운 Bitnami 사용 제한에 대해 설명하며, Docker를 사용해 쉽게 마이그레이션할 수 있는 방법을 소개합니다. Bitnami는 오랜 기간 오픈 소스 및 클라우드 네이티브 커뮤니티에서 중요한 역할을 했으며, 개발자와 운영자가 인기 있는 애플리케이션을 신뢰할 수 있는 사전 구축된 컨테이너 이미지와 Helm 차트를 통해 쉽게 배포할 수 있도록 도왔습니다. 이 글은 Bitnami의 표준화 작업 덕분에 많은 팀들이 WordPress나 PostgreSQL 같은 애플리케이션을 설치하고 업데이트하는 데 혜택을 받아왔음을 인정하며, 새로운 제한 사항에 대응하기 위한 방법을 제안합니다.
👉 [자세히 보기](https://www.docker.com/blog/broadcoms-new-bitnami-restrictions-migrate-easily-with-docker/)

## 🔹 Java - The Inside Java Newsletter: Java 25, AI World, JavaOne 2026!
8월 2025년자 Inside Java 뉴스레터는 9월에 출시될 Java 25, 10월 Oracle AI World의 Java 세션, 2026년 3월에 열릴 JavaOne에 대해 다룹니다. 또한 Java 사용자 그룹의 최신 업데이트, 커뮤니티 이벤트, 엔지니어링 및 커뮤니티 팟캐스트, Java 플랫폼 그룹 개발자들의 기술 콘텐츠도 포함되어 있습니다. Inside Java 뉴스레터는 Java 개발자 관계 팀에서 제작하며, 다양한 멀티미디어 콘텐츠를 제공하는 learn.java, dev.java, inside.java를 방문해 보세요. 뉴스레터 아카이브를 확인하고 구독하거나 친구에게 공유하세요.
👉 [자세히 보기](https://inside.java/2025/09/02/inside-java-newsletter/)

## 🔹 Golang - Testing Time (and other asynchronicities)
이 기술 블로그 글은 비동기 코드 테스트 방법과 `testing/synctest` 패키지에 대한 탐구를 다루고 있습니다. 이는 GopherCon Europe 2025에서 같은 제목으로 진행된 발표를 기반으로 작성되었습니다. 비동기 코드의 특성을 고려한 테스트 기법과 관련 도구에 대해 설명합니다.
👉 [자세히 보기](https://go.dev/blog/testing-time)

## 🔹 Helm - Helm @ KubeCon + CloudNativeCon EU '25
이번 주 4월 1일부터 4일까지 영국 런던에서 열리는 KubeCon + CloudNativeCon EU '25에 Helm 팀이 참가합니다. Helm 4가 올해 말 출시 예정이므로, 이번 행사에서 유지관리자들과의 대화에 참여해보세요. 행사 기간 동안 열리는 Helm 관련 활동에 대한 자세한 내용은 링크를 참조하세요.
👉 [자세히 보기](https://helm.sh/blog/helm-at-kubecon-eu-25/)

