# 🛠️ 2025-06-03 기술 업데이트 요약

## 🔹 Kubernetes - Start Sidecar First: How To Avoid Snags
이 기술 블로그는 Kubernetes에서 사이드카 컨테이너를 메인 애플리케이션보다 먼저 시작하는 방법을 설명합니다. Kubernetes v1.29.0부터는 `.spec.initContainers` 필드에 사이드카 컨테이너를 정의할 수 있으며, 이 경우 메인 애플리케이션보다 항상 먼저 시작됩니다. 그러나, 사이드카가 완전히 실행되고 준비되기 전까지 메인 애플리케이션의 시작을 지연시키는 것은 복잡할 수 있습니다. 이 글에서는 `readinessProbe`, `livenessProbe`, `startupProbe`, 그리고 `postStart` 라이프사이클 훅과 같은 다양한 접근 방식을 설명하고, 각각의 경우 메인 애플리케이션이 사이드카에 의존하는 상황에서의 효과를 분석합니다. 결론적으로, 메인 애플리케이션이 사이드카가 준비될 때까지 기다리도록 하려면 적절한 Pod 정의 커스터마이징이 필요하며, 블로그는 이를 위한 다양한 방법을 제시하고 있습니다.
👉 [자세히 보기](https://kubernetes.io/blog/2025/06/03/start-sidecar-first/)

## 🔹 Spring Boot - Spring Cloud 2022.0.11 (aka Kilburn) Has Been Released
Spring Cloud 팀은 Spring Cloud 2022.0.11 릴리즈가 지원 고객을 위해 출시되었음을 발표했습니다. 이 릴리즈는 Spring Boot 3.0.20 및 3.1.17과 호환되며, 다양한 Spring Cloud 구성 요소의 의존성 업그레이드가 포함되어 있습니다. 특히 Spring Cloud Config와 Spring Cloud Gateway는 각각 CVE-2025-22232 및 CVE-2025-41235 보안 취약점을 수정했습니다. 이 릴리즈는 https://packages.broadcom.com에서 확인할 수 있습니다.
👉 [자세히 보기](https://spring.io/blog/2025/06/02/spring-cloud-2022-0-11-aka-kilburn-has-been-released)

## 🔹 Docker - Introducing Docker Hardened Images: Secure, Minimal, and Ready for Production
이 기술 블로그 글은 Docker의 강화된 이미지(Docker Hardened Images)를 소개하는 내용입니다. Docker는 개발자들이 소프트웨어를 효율적이고 안전하게 구축, 공유, 실행할 수 있도록 하는 데 중점을 두고 있습니다. Docker Hub는 매달 1400만 개 이상의 이미지와 110억 건 이상의 다운로드를 기록하며 전 세계적으로 소프트웨어 배포를 지원하고 있습니다. 이러한 규모 덕분에 현대 소프트웨어가 어떻게 구축되는지에 대한 독특한 통찰을 제공할 수 있습니다. 이 글에서는 Docker의 강화된 이미지가 어떻게 더 안전하고, 최소화된 구성으로 프로덕션 환경에서 사용될 준비가 되어 있는지를 설명하고 있습니다.
👉 [자세히 보기](https://www.docker.com/blog/introducing-docker-hardened-images/)

## 🔹 Java - JEP targeted to JDK 25: 506: Scoped Values
제목이 "JEP targeted to JDK 25: 506: Scoped Values"인 기술 블로그 글은 JDK 25 버전에 포함될 예정인 JEP 506, 즉 "Scoped Values"에 대한 내용을 다루고 있습니다. 이 JEP는 특정 범위 내에서 값을 안전하게 관리하고 사용할 수 있도록 하는 기능을 소개합니다. 해당 블로그 글에서는 이 기능의 주요 목적과 장점에 대해 설명하고 있으며, JEP 506이 JDK 25에 포함될 것임을 알리고 있습니다. 더 자세한 내용은 제공된 링크를 통해 확인할 수 있습니다.
👉 [자세히 보기](https://inside.java/2025/06/02/jep506-target-jdk25/)

## 🔹 Golang - Go Cryptography Security Audit
제목: Go 암호화 보안 감사  
요약: Trail of Bits가 Go의 암호화 라이브러리에 대한 감사를 수행했습니다.  
링크: https://go.dev/blog/tob-crypto-audit

Trail of Bits가 Go 프로그래밍 언어의 암호화 라이브러리에 대한 보안 감사를 진행했습니다. 이 감사는 라이브러리의 보안성을 평가하고 잠재적인 취약점을 식별하는 데 중점을 두었습니다. 감사 결과는 Go의 암호화 기능을 개선하고 강화하는 데 기여할 것입니다.
👉 [자세히 보기](https://go.dev/blog/tob-crypto-audit)

## 🔹 Helm - Helm @ KubeCon + CloudNativeCon EU '25
제목: Helm @ KubeCon + CloudNativeCon EU '25

요약: Helm 팀이 4월 1일부터 4일까지 영국 런던에서 열리는 KubeCon + CloudNativeCon EU '25에 참가합니다. 올해 말 출시 예정인 Helm 4에 대한 논의에 참여할 수 있는 기회가 있으며, 우리 팀의 발표 세션과 프로젝트 파빌리온 내 Helm 부스에서 유지 관리자들과 대화할 수 있습니다. 주간 동안 진행되는 모든 Helm 관련 활동에 대한 자세한 내용은 링크를 참조하세요.
👉 [자세히 보기](https://helm.sh/blog/helm-at-kubecon-eu-25/)

