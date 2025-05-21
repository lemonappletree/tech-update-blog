# 🛠️ 2025-05-21 기술 업데이트 요약

## 🔹 Kubernetes - Kubernetes v1.33: In-Place Pod Resize Graduated to Beta
Kubernetes v1.33 버전에서 "인플레이스 Pod 리사이즈" 기능이 베타 버전으로 승격되었습니다. 이 기능은 처음 v1.27에 알파 버전으로 도입되었으며, 이제 기본적으로 활성화됩니다. 이 기능은 실행 중인 Pod의 CPU 및 메모리 자원을 재시작 없이 조정할 수 있어, 리소스 관리의 유연성을 높이고 중단을 최소화합니다. 베타 버전에서는 사용자 경험 개선, 안정성 강화, 사이드카 컨테이너 지원 등이 추가되었습니다. 향후에는 VerticalPodAutoscaler(VPA)와의 통합 및 사용자의 피드백 반영을 통해 기능을 더욱 발전시킬 계획입니다. Kubernetes 커뮤니티는 이 기능을 통해 더 효율적이고 탄력적인 애플리케이션 구축을 기대하고 있습니다.
👉 [자세히 보기](https://kubernetes.io/blog/2025/05/16/kubernetes-v1-33-in-place-pod-resize-beta/)

## 🔹 Spring Boot - Spring for Apache Pulsar 1.1.12 and 1.2.6 are now available
Spring for Apache Pulsar의 버전 1.1.12와 1.2.6이 출시되어 Maven Central에서 사용할 수 있게 되었습니다. 이 릴리스는 각각 다가오는 Spring Boot 3.3.12 및 3.4.6 릴리스에 포함될 예정입니다. 자세한 내용은 릴리스 노트를 참고하세요.
👉 [자세히 보기](https://spring.io/blog/2025/05/21/spring-for-apache-pulsar-1-1-12-and-1-2-6-are-now-available)

## 🔹 Docker - Introducing Docker Hardened Images: Secure, Minimal, and Ready for Production
이 기술 블로그 글은 Docker의 새로운 강화 이미지(Docker Hardened Images)의 도입에 대해 설명하고 있습니다. Docker는 개발자들이 효율적이고 안전하게 소프트웨어를 구축, 공유, 실행할 수 있도록 지원해 왔으며, Docker Hub는 매달 140억 건 이상의 다운로드와 1,400만 개 이상의 이미지를 통해 글로벌 소프트웨어 배포를 지원하고 있습니다. 이러한 규모는 현대 소프트웨어가 어떻게 구축되는지를 잘 보여주며, Docker는 이를 바탕으로 보안과 최소화를 강화한 프로덕션 준비 이미지를 제공하고자 합니다.
👉 [자세히 보기](https://www.docker.com/blog/introducing-docker-hardened-images/)

## 🔹 Java - Towards a JSON API for the JDK
이 기술 블로그 글은 JDK를 위한 JSON API 개발에 대한 아이디어와 계획을 다루고 있습니다. JSON API는 데이터 교환의 표준화된 방식을 제공하여 개발자들이 더 쉽게 JSON 데이터를 처리할 수 있도록 돕는 것을 목표로 합니다. 이 글에서는 JDK에 JSON API를 도입하기 위한 초기 단계의 논의와 방향성을 공유하고 있습니다.
👉 [자세히 보기](https://inside.java/2025/05/20/json-api-jdk/)

## 🔹 Golang - Go Cryptography Security Audit
제목: Go 암호화 보안 감사

요약: Go 언어의 암호화 라이브러리에 대한 보안 감사가 Trail of Bits에 의해 수행되었습니다.
👉 [자세히 보기](https://go.dev/blog/tob-crypto-audit)

## 🔹 Helm - Helm @ KubeCon + CloudNativeCon EU '25
블로그 글 요약: Helm 팀이 2025년 4월 1일부터 4일까지 영국 런던에서 열리는 KubeCon + CloudNativeCon EU '25에 참가합니다. 올해 말 출시 예정인 Helm 4에 대한 논의에 참여할 수 있는 기회가 마련되어 있으며, 발표 세션과 프로젝트 파빌리온 내 Helm 부스에서 유지관리자들과 대화할 수 있습니다. 주간 동안 진행되는 모든 Helm 관련 활동에 대한 자세한 내용은 링크를 참조하세요.
👉 [자세히 보기](https://helm.sh/blog/helm-at-kubecon-eu-25/)

