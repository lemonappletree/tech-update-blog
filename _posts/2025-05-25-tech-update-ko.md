# 🛠️ 2025-05-25 기술 업데이트 요약

## 🔹 Kubernetes - Kubernetes v1.33: In-Place Pod Resize Graduated to Beta
Kubernetes 프로젝트는 v1.33 릴리스에서 "인플레이스 Pod 리사이즈" 기능이 베타로 발전하여 기본적으로 활성화된다고 발표했습니다. 이 기능은 Kubernetes v1.27에서 처음 알파로 도입되었으며, Pod를 다시 시작하지 않고도 실행 중인 Pod의 CPU 및 메모리 리소스를 조정할 수 있어, 상태 저장 애플리케이션, 배치 작업 등에서의 중단을 줄이고 리소스 활용도를 높입니다. 베타 단계로 발전하면서 사용자 경험을 개선하고 안정성을 향상시켰으며, Pod 리사이즈를 위한 새로운 하위 리소스를 도입했습니다. 이 기능은 Kubernetes 커뮤니티의 피드백을 통해 더욱 발전할 예정이며, VerticalPodAutoscaler(VPA)와의 통합도 진행 중입니다. v1.33부터 이 기능을 실험해볼 수 있으며, 사용자 피드백은 기능 개선에 큰 도움이 됩니다.
👉 [자세히 보기](https://kubernetes.io/blog/2025/05/16/kubernetes-v1-33-in-place-pod-resize-beta/)

## 🔹 Spring Boot - Spring for Apache Pulsar 1.1.12 and 1.2.6 are now available
Spring 팀과 기여자들을 대표하여, Apache Pulsar를 위한 Spring 버전 1.1.12와 1.2.6이 출시되어 Maven Central에서 이용 가능하다는 소식을 전합니다. 이 릴리스들은 각각 다가오는 Spring Boot 3.3.12와 3.4.6 릴리스에 포함될 예정입니다. 자세한 내용은 릴리스 노트를 참조하세요.
👉 [자세히 보기](https://spring.io/blog/2025/05/25/spring-for-apache-pulsar-1-1-12-and-1-2-6-are-now-available)

## 🔹 Docker - Introducing Docker Hardened Images: Secure, Minimal, and Ready for Production
제목: Docker 강화 이미지 소개: 안전하고 최소화된 프로덕션 준비 완료
요약: Docker는 처음부터 개발자들이 소프트웨어를 효율적이고 안전하게 구축, 공유 및 실행할 수 있도록 지원하는 데 중점을 두었습니다. 오늘날 Docker Hub는 매달 1400만 개 이상의 이미지와 110억 회 이상의 다운로드로 전 세계적으로 소프트웨어 전달을 지원하고 있습니다. 이러한 규모 덕분에 현대 소프트웨어가 구축되는 방식을 독특한 관점에서 볼 수 있게 되었습니다. 이 글에서는 Docker의 강화 이미지를 소개하며, 이 이미지는 보안을 강화하고 최소화된 형태로 프로덕션 환경에 바로 사용할 수 있도록 준비되어 있습니다.
👉 [자세히 보기](https://www.docker.com/blog/introducing-docker-hardened-images/)

## 🔹 Java - Pattern Matching in Java: Better Code, Better APIs
제목: 자바의 패턴 매칭: 더 나은 코드, 더 나은 API

요약: 자바 1.0부터 switch와 instanceof는 데이터 분석의 중요한 도구였습니다. 현대에 이르러 이 구조들은 완전한 패턴 매칭을 가능하게 하여, 자바 개발자들이 더 깔끔한 구현 코드를 작성할 수 있도록 발전했습니다. 이 글에서는 switch와 instanceof의 현재 역할을 탐구하고, 패턴 매칭이 API 개발 및 직렬화와 같은 자바의 핵심 기능들에 어떤 영향을 미칠지 논의합니다.
👉 [자세히 보기](https://inside.java/2025/05/24/javaone-pattern-matching/)

## 🔹 Golang - Go Cryptography Security Audit
제목: Go 암호화 보안 감사

요약: Go 언어의 암호화 라이브러리가 Trail of Bits에 의해 보안 감사를 받았습니다.
👉 [자세히 보기](https://go.dev/blog/tob-crypto-audit)

## 🔹 Helm - Helm @ KubeCon + CloudNativeCon EU '25
블로그 글 요약: Helm 팀이 오는 4월 1일부터 4일까지 영국 런던에서 열리는 KubeCon + CloudNativeCon EU '25에 참가합니다. 올해 말 출시 예정인 Helm 4에 대한 논의에 참여할 수 있는 기회가 있으며, 팀의 발표 세션과 Project Pavilion의 Helm 부스를 방문해보세요. 이번 주에 진행되는 Helm 관련 활동에 대한 자세한 사항은 링크에서 확인할 수 있습니다.
👉 [자세히 보기](https://helm.sh/blog/helm-at-kubecon-eu-25/)

