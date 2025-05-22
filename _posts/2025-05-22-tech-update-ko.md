# 🛠️ 2025-05-22 기술 업데이트 요약

## 🔹 Kubernetes - Kubernetes v1.33: In-Place Pod Resize Graduated to Beta
Kubernetes v1.33 릴리스에서 '인플레이스 Pod 리사이즈' 기능이 베타 버전으로 업데이트되어 기본적으로 활성화됩니다. 이 기능은 Kubernetes의 리소스 관리를 더욱 유연하고 덜 방해적으로 만들어 줍니다. 기존에는 컨테이너의 CPU나 메모리 리소스를 변경하려면 Pod를 재시작해야 했지만, 이제는 실행 중인 Pod에서도 이러한 리소스를 변경할 수 있습니다. 이는 상태 기반 애플리케이션, 배치 작업, 재시작에 민감한 워크로드에 큰 이점을 제공합니다. 베타 버전에서는 사용자의 피드백을 반영하여 안정성이 향상되었고, 사용자 경험이 개선되었습니다. 또한, 수직적 확장을 위한 VerticalPodAutoscaler(VPA)와의 통합 작업도 진행 중입니다. 사용자는 v1.33 클러스터에서 이 기능을 실험해볼 수 있으며, 피드백은 Kubernetes 커뮤니티에 큰 도움이 됩니다.
👉 [자세히 보기](https://kubernetes.io/blog/2025/05/16/kubernetes-v1-33-in-place-pod-resize-beta/)

## 🔹 Spring Boot - Spring for Apache Pulsar 1.1.12 and 1.2.6 are now available
Apache Pulsar를 위한 Spring의 버전 1.1.12와 1.2.6이 출시되어 Maven Central에서 사용할 수 있게 되었습니다. 이 버전들은 각각 다가오는 Spring Boot 3.3.12와 3.4.6 릴리스에 포함될 예정입니다. 자세한 내용은 릴리스 노트를 참고하세요.
👉 [자세히 보기](https://spring.io/blog/2025/05/22/spring-for-apache-pulsar-1-1-12-and-1-2-6-are-now-available)

## 🔹 Docker - Introducing Docker Hardened Images: Secure, Minimal, and Ready for Production
이 기술 블로그 글은 Docker가 새롭게 선보이는 'Docker Hardened Images'에 대해 소개하고 있습니다. Docker는 처음부터 개발자들이 소프트웨어를 효율적이고 안전하게 구축, 공유 및 실행할 수 있도록 지원하는 데 중점을 두어 왔습니다. 오늘날 Docker Hub는 매월 1400만 개 이상의 이미지와 110억 번 이상의 다운로드를 처리하며, 전 세계적으로 소프트웨어 배포를 지원하고 있습니다. 이러한 규모는 현대 소프트웨어가 어떻게 구축되는지를 독특한 관점에서 볼 수 있게 해줍니다. 'Docker Hardened Images'는 보안이 강화된 최소화된 이미지로, 프로덕션 환경에서 바로 사용할 수 있도록 설계되었습니다.
👉 [자세히 보기](https://www.docker.com/blog/introducing-docker-hardened-images/)

## 🔹 Java - Towards a JSON API for the JDK
이 기술 블로그 글은 JDK를 위한 JSON API 개발에 대한 생각과 계획을 공유하는 내용입니다. JDK에 JSON API를 도입함으로써 개발자들이 더 쉽게 JSON 데이터를 처리할 수 있도록 돕고자 하는 목표를 가지고 있습니다.
👉 [자세히 보기](https://inside.java/2025/05/20/json-api-jdk/)

## 🔹 Golang - Go Cryptography Security Audit
제목: Go 암호화 보안 감사

요약: Go의 암호화 라이브러리가 Trail of Bits에 의해 감사를 받았습니다.
👉 [자세히 보기](https://go.dev/blog/tob-crypto-audit)

## 🔹 Helm - Helm @ KubeCon + CloudNativeCon EU '25
제목: Helm @ KubeCon + CloudNativeCon EU '25

요약: Helm 팀이 4월 1일부터 4일까지 영국 런던에서 열리는 KubeCon + CloudNativeCon EU '25에 참가합니다. 올해 말 출시 예정인 Helm 4에 대한 논의에 참여할 수 있는 기회로, 발표 세션과 프로젝트 파빌리온의 Helm 부스에서 유지관리자들과의 대화를 나눌 수 있습니다. 이번 주 동안 진행되는 모든 Helm 관련 활동에 대한 자세한 내용은 링크를 참조하세요.
👉 [자세히 보기](https://helm.sh/blog/helm-at-kubecon-eu-25/)

