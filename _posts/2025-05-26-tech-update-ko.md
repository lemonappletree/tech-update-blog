# 🛠️ 2025-05-26 기술 업데이트 요약

## 🔹 Kubernetes - Kubernetes v1.33: In-Place Pod Resize Graduated to Beta
이 블로그 글은 Kubernetes 프로젝트에서 인플레이스(In-Place) 파드 리사이즈 기능이 v1.33 버전에서 베타 단계로 승격되었음을 알립니다. 이 기능은 기존에는 컨테이너의 CPU나 메모리 할당을 변경하려면 파드를 재시작해야 했으나, 이제는 실행 중인 파드 내에서 이러한 리소스를 조정할 수 있게 합니다. 이를 통해 상태 저장 애플리케이션이나 배치 작업 등에서 발생할 수 있는 중단을 줄이고, 리소스 활용도를 개선할 수 있습니다. 또한, 알파 버전 이후 사용자 경험 개선 및 안정성 강화를 위한 다양한 변경 사항이 적용되었습니다. 앞으로도 기능의 안정성과 성능 개선, VerticalPodAutoscaler 통합 등을 목표로 개발이 계속될 것입니다. 사용자는 이 기능을 통해 보다 효율적이고 회복력 있는 애플리케이션을 구축할 수 있게 됩니다.
👉 [자세히 보기](https://kubernetes.io/blog/2025/05/16/kubernetes-v1-33-in-place-pod-resize-beta/)

## 🔹 Spring Boot - Spring for Apache Pulsar 1.1.12 and 1.2.6 are now available
Spring for Apache Pulsar의 버전 1.1.12와 1.2.6이 출시되어 Maven Central에서 이용 가능합니다. 이 버전들은 각각 다가오는 Spring Boot 3.3.12와 3.4.6 릴리스에 포함될 예정입니다. 자세한 내용은 릴리스 노트를 참고하세요.
👉 [자세히 보기](https://spring.io/blog/2025/05/26/spring-for-apache-pulsar-1-1-12-and-1-2-6-are-now-available)

## 🔹 Docker - Introducing Docker Hardened Images: Secure, Minimal, and Ready for Production
이 블로그 글은 Docker가 새롭게 소개한 'Docker Hardened Images'에 대한 내용을 다루고 있습니다. Docker는 개발자들이 소프트웨어를 효율적이고 안전하게 구축, 공유, 실행할 수 있도록 지원해 왔으며, 현재 Docker Hub는 매달 1400만 개 이상의 이미지와 110억 이상의 다운로드를 통해 전 세계적으로 소프트웨어 전달을 지원하고 있습니다. 이러한 규모 덕분에 현대 소프트웨어가 어떻게 구축되는지에 대한 독특한 관점을 제공할 수 있습니다. Hardened Images는 이와 같은 Docker의 철학을 바탕으로 보안성과 최소화된 이미지를 통해 프로덕션 환경에서의 사용을 염두에 두고 설계되었습니다.
👉 [자세히 보기](https://www.docker.com/blog/introducing-docker-hardened-images/)

## 🔹 Java - Pattern Matching in Java: Better Code, Better APIs
글 제목은 "자바의 패턴 매칭: 더 나은 코드, 더 나은 API"입니다. Java 1.0부터 switch와 instanceof는 데이터 분석의 중요한 도구였습니다. 현대에 이르러, 이러한 구조는 완전한 패턴 매칭을 가능하게 하여 Java 개발자들이 더 깔끔한 구현 코드를 작성할 수 있도록 발전했습니다. 이 글에서는 switch와 instanceof의 현재 역할을 탐구하고, 패턴 매칭이 API 개발과 직렬화와 같은 Java의 핵심 기능의 미래에 어떤 영향을 미칠지 논의합니다.
👉 [자세히 보기](https://inside.java/2025/05/24/javaone-pattern-matching/)

## 🔹 Golang - Go Cryptography Security Audit
제목: Go 암호화 보안 감사

요약: Go 언어의 암호화 라이브러리에 대해 Trail of Bits에서 보안 감사를 진행했습니다.
👉 [자세히 보기](https://go.dev/blog/tob-crypto-audit)

## 🔹 Helm - Helm @ KubeCon + CloudNativeCon EU '25
블로그 글 요약: Helm 팀이 2025년 4월 1일부터 4일까지 영국 런던에서 열리는 KubeCon + CloudNativeCon EU '25에 참가합니다. 올해 말 출시 예정인 Helm 4에 대해 이야기하고, 유지 관리자들과의 대화에 참여할 수 있는 발표 세션과 Helm 부스를 방문해보세요. 주간 동안 진행되는 모든 Helm 관련 활동에 대한 자세한 내용은 블로그에서 확인할 수 있습니다.
👉 [자세히 보기](https://helm.sh/blog/helm-at-kubecon-eu-25/)

