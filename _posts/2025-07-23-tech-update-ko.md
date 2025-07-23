# 🛠️ 2025-07-23 기술 업데이트 요약

## 🔹 Kubernetes - Post-Quantum Cryptography in Kubernetes
이 기술 블로그 글은 양자 컴퓨팅의 발전으로 인해 암호화 분야가 큰 변화를 맞이하고 있으며, 현재의 암호화 표준이 양자 컴퓨터에 의해 깨질 가능성이 있다는 우려를 다루고 있습니다. 이에 대한 해결책으로 **양자 이후 암호화(Post-Quantum Cryptography, PQC)**가 제시됩니다. 글에서는 PQC가 TLS 및 Kubernetes 생태계에 미치는 영향을 설명하고, 현재 Kubernetes에서의 PQC 상태와 향후 클러스터에 대한 함의를 논의합니다.

PQC는 전통적 및 양자 컴퓨터 공격에 모두 안전하다고 여겨지는 암호 알고리즘을 의미합니다. 특히, 양자 컴퓨터가 RSA 및 타원 곡선 암호화(ECC) 같은 공통 공개 키 암호화 시스템을 효과적으로 깨뜨릴 수 있는 가능성 때문에 산업계에서는 PQC 알고리즘의 표준화 및 채택을 적극적으로 추진 중입니다. 예를 들어, NIST는 Module-Lattice Key Encapsulation Mechanism(ML-KEM)이라는 알고리즘을 표준화했습니다.

TLS에서 PQC의 채택은 하이브리드 키 교환 메커니즘에서 시작되고 있으며, 이는 기존의 알고리즘과 PQC 알고리즘을 결합하여 보안을 강화합니다. Kubernetes도 Go 언어의 업데이트를 통해 기본적으로 하이브리드 PQC 키 교환을 지원하게 되었으며, 이는 큰 발표 없이 이루어진 중요한 진전입니다.

그러나 Go 버전 불일치로 인한 문제, 초기 패킷 크기 제한, 그리고 PQC 디지털 서명의 도입 지연 등 여러 실질적 문제도 존재합니다. 글은 이러한 문제들을 해결하고 장기적인 보안을 보장하기 위해 Kubernetes 유지보수자 및 기여자들이 최신 정보를 유지해야 한다고 강조합니다.
👉 [자세히 보기](https://kubernetes.io/blog/2025/07/18/pqc-in-k8s/)

## 🔹 Spring Boot - Spring Authorization Server 2.0.0-M1 available now
Spring Authorization Server 팀과 기여자들을 대신하여 2.0.0-M1 버전의 마일스톤 릴리스를 발표하게 되어 기쁩니다. 자세한 사항은 [릴리스 노트](https://github.com/spring-projects/spring-authorization-server/releases/tag/2.0.0-M1)를 참조하십시오. Spring Authorization Server를 시작하려면 [시작하기](https://docs.spring.io/spring-authorization-server/reference/getting-started.html) 문서와 [샘플](https://github.com/spring-projects/spring-authorization-server/tree/main/samples)을 참고하여 설정 및 구성에 익숙해지십시오. 프로젝트 페이지와 GitHub 이슈도 제공됩니다.
👉 [자세히 보기](https://spring.io/blog/2025/07/22/spring-authorization-server-2-0-0-M1-available-now)

## 🔹 Docker - Compose Editing Evolved: Schema-Driven and Context-Aware
제목: 발전된 Compose 편집: 스키마 기반 및 컨텍스트 인식

요약: 매일 수천 명의 개발자들이 Compose 파일을 생성하고 편집하고 있습니다. Docker에서는 Docker Compose에 새로운 제공자 서비스 기능 등을 추가하여 Docker Model Runner를 통해 AI 모델을 멀티 컨테이너 애플리케이션의 일부로 실행할 수 있도록 하는 등 기능을 지속적으로 추가하고 있습니다. Docker는 Compose에 대한 최상의 편집 경험을 제공하는 것이 중요하다고 생각합니다.
👉 [자세히 보기](https://www.docker.com/blog/compose-editing-evolved-schema-driven-and-context-aware/)

## 🔹 Java - A Sneak Peek at the Stable Values API
제목: 안정 값 API 미리 보기

요약: 내부 JDK 클래스는 값이 최대 한 번만 변경되는 스칼라 및 배열 필드를 표시하기 위해 jdk.internal.vm.annotation.@Stable 주석을 많이 활용합니다. 이는 중요한 성능, 에너지 효율성 및 유연성 이점을 제공합니다. 그러나 강력한 @Stable 주석은 Java 애플리케이션에서 직접 사용할 수 없어 그 적용 범위가 제한됩니다. 안정 값 API는 `@Stable` 주석 주위에 안전한 래퍼를 제공하여 내부 코드와 클라이언트 코드 간의 불균형을 해소합니다. 따라서 @Stable의 모든 중요한 이점이 일반 Java 개발자 및 서드파티 라이브러리 개발자에게 제공됩니다. 요소가 상수 값인 것과 동일한 성능으로 지연 초기화된 리스트와 맵을 만드는 방법을 알아보세요!
👉 [자세히 보기](https://inside.java/2025/07/22/javaone-stablevalues/)

## 🔹 Golang - The FIPS 140-3 Go Cryptographic Module
이 블로그 글은 Go 프로그래밍 언어에 내장된 FIPS 140-3 준수 모드가 추가된 것을 소개합니다. FIPS 140-3은 암호 모듈의 보안 표준으로, 이제 Go에서 이를 지원하는 네이티브 모드를 사용할 수 있게 되었습니다. 이를 통해 Go 사용자들은 보다 안전한 암호화 환경을 구현할 수 있습니다.
👉 [자세히 보기](https://go.dev/blog/fips140)

## 🔹 Helm - Helm @ KubeCon + CloudNativeCon EU '25
블로그 글 요약: Helm 팀이 올해 4월 1일부터 4일까지 영국 런던에서 열리는 KubeCon + CloudNativeCon EU '25에 참가합니다. 올해 말 출시 예정인 Helm 4에 대한 논의가 진행될 예정이니, 발표 세션과 Helm 부스에서 유지관리자들과 대화에 참여해 보세요. 주간 동안 진행될 모든 Helm 관련 활동에 대한 자세한 내용은 블로그에서 확인할 수 있습니다.
👉 [자세히 보기](https://helm.sh/blog/helm-at-kubecon-eu-25/)

