# 🛠️ 2025-06-25 기술 업데이트 요약

## 🔹 Kubernetes - Image Compatibility In Cloud Native Environments
이 블로그 글은 클라우드 네이티브 환경에서 이미지 호환성의 중요성과 이를 해결하기 위한 접근 방식을 설명합니다. 특히, 통신, 고성능 컴퓨팅, AI 등 특정 시스템 요구 사항을 만족해야 하는 산업에서는 컨테이너화된 애플리케이션이 특정 운영체제 환경이나 하드웨어 의존성을 가질 수 있습니다. Kubernetes의 Node Feature Discovery(NFD)는 클러스터 노드의 하드웨어 및 시스템 기능을 자동으로 감지하고 보고하여 이러한 요구 사항을 충족하는 노드에 워크로드를 스케줄링하는 데 도움을 줍니다.

이미지 호환성 명세의 필요성을 강조하며, 호스트 운영체제와 컨테이너 이미지 간의 의존성을 효과적으로 표현할 수 있는 방안이 요구됩니다. 이를 위해 Open Containers Initiative(OCI)에서는 이미지 호환성 메타데이터를 표준화하는 작업을 진행 중입니다. Kubernetes의 NFD 프로젝트는 이러한 호환성 요구 사항을 표현하고, 자동 검증을 통해 컨테이너 스케줄링을 최적화하는 데 기여하고 있습니다.

블로그는 또한 멀티 클라우드 및 하이브리드 클라우드 환경에서의 호환성 문제를 논의하고, 이를 해결하기 위한 이미지 호환성 이니셔티브의 구현 방안을 설명합니다. 마지막으로 Kubernetes Node Feature Discovery 프로젝트에 참여하여 이미지 호환성 API와 도구의 설계 및 개발에 기여할 수 있다고 안내합니다.
👉 [자세히 보기](https://kubernetes.io/blog/2025/06/25/image-compatibility-in-cloud-native-environments/)

## 🔹 Spring Boot - This Week in Spring - June 24th, 2025
이번 주 Spring 블로그 글은 2025년 6월 24일자 'This Week in Spring'입니다. 이번 주에는 SpringOne 이벤트가 라스베가스에서 열리며, 저자는 Spring AI와 Spring Security에 관한 세션과 키노트에 참여한다고 합니다. 주요 업데이트로는 Spring Tools 4.31.0, Spring Framework의 보안 패치 릴리스, Spring Authorization Server 및 Spring Web Services의 새로운 버전 출시, Spring Vault 4.0.0.M1, Spring for Apache Pulsar의 새로운 버전 출시, Spring Data의 릴리스, 그리고 Spring Framework 7.0.0 M6의 출시가 있습니다. 또한 작가는 VMware Tanzu에서 Spring AI를 이용한 AI 생산에 관한 글을 작성했으며, Rod Johnson의 새로운 AI 프레임워크 'Embabel'도 소개됩니다.
👉 [자세히 보기](https://spring.io/blog/2025/06/24/this-week-in-spring-june-24-2025)

## 🔹 Docker - Docker State of App Dev: Security
이 블로그 글은 Docker의 2025년 애플리케이션 개발 보고서에서 보안에 대한 주요 내용을 다루고 있습니다. 소프트웨어 개발의 변화하는 환경에서 보안은 더 이상 특정 전문가들만의 영역이 아니며, 팀 전체가 함께 책임져야 하는 분야임을 강조합니다. 특히 취약점이 발견될 때 팀워크가 중요하다는 점을 강조하며, 이와 관련된 여섯 가지 보안 시사점을 제시하고 있습니다.
👉 [자세히 보기](https://www.docker.com/blog/docker-state-of-app-dev-security/)

## 🔹 Java - Episode 38 “Integrity by Default” with Ron Pressler
블로그 글은 오라클의 자바 아키텍트이자 프로젝트 룸(Project Loom)의 리더인 론 프레슬러와 니콜라이 파를로그가 "기본값으로서의 무결성(Integrity by Default)"에 관한 지속적인 노력에 대해 논의한 내용을 다룹니다. 이 에피소드에서는 자바 개발의 신뢰성을 높이기 위한 다양한 시도와 프로젝트 룸의 역할에 대해 다루고 있습니다.
👉 [자세히 보기](https://inside.java/2025/06/24/podcast-038/)

## 🔹 Golang - [ On | No ] syntactic support for error handling
제목: [ On | No ] 문법적 오류 처리 지원
요약: Go 팀은 오류 처리 지원에 대한 계획을 논의하고 있습니다.
👉 [자세히 보기](https://go.dev/blog/error-syntax)

## 🔹 Helm - Helm @ KubeCon + CloudNativeCon EU '25
제목: Helm @ KubeCon + CloudNativeCon EU '25

요약: Helm 팀이 2025년 4월 1일부터 4일까지 영국 런던에서 열리는 KubeCon + CloudNativeCon EU에 참석합니다. 올해 말 출시 예정인 Helm 4에 대한 논의가 있을 예정이니, 팀의 발표 세션과 프로젝트 파빌리온 내 Helm 부스에서 유지관리자들과의 대화에 참여해 보세요. 주간 동안 진행되는 모든 Helm 관련 활동에 대한 자세한 내용은 링크를 참조하세요.
👉 [자세히 보기](https://helm.sh/blog/helm-at-kubecon-eu-25/)

