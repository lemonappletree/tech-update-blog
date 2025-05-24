# 🛠️ 2025-05-24 기술 업데이트 요약

## 🔹 Kubernetes - Kubernetes v1.33: In-Place Pod Resize Graduated to Beta
이 기술 블로그 글은 Kubernetes 프로젝트에서 "In-Place Pod Resize" 기능이 Kubernetes v1.33 버전에서 베타로 승격되었음을 알리는 내용입니다. 이 기능은 컨테이너의 CPU와 메모리 자원을 재시작 없이 조정할 수 있게 하여, 특히 상태 유지 애플리케이션이나 재시작에 민감한 작업에 유용합니다. 기존에는 리소스를 변경하려면 Pod를 재시작해야 했으나, 이제는 실행 중인 Pod의 리소스를 직접 변경할 수 있습니다. 베타 버전으로 발전하면서 안정성과 사용자 경험이 크게 개선되었고, 사이드카 컨테이너에 대한 지원도 추가되었습니다. 향후에는 VerticalPodAutoscaler와의 통합, 기능의 안정화 및 성능 향상, 사용자 피드백 수집 등이 예정되어 있습니다. 사용자는 Kubernetes v1.33에서 이 기능을 시도해 볼 수 있으며, 피드백을 통해 기능 개선에 기여할 수 있습니다.
👉 [자세히 보기](https://kubernetes.io/blog/2025/05/16/kubernetes-v1-33-in-place-pod-resize-beta/)

## 🔹 Spring Boot - Spring for Apache Pulsar 1.1.12 and 1.2.6 are now available
제목: Spring for Apache Pulsar 1.1.12 및 1.2.6 출시  
요약: 팀과 기여자들을 대표하여, Spring for Apache Pulsar 버전 1.1.12와 1.2.6이 출시되어 이제 Maven Central에서 이용 가능하다고 발표했습니다. 이 릴리스는 각각 다가오는 Spring Boot 3.3.12 및 3.4.6 릴리스에 포함될 예정입니다. 자세한 내용은 릴리스 노트(1.1.12 및 1.2.6)를 참조하세요.
👉 [자세히 보기](https://spring.io/blog/2025/05/24/spring-for-apache-pulsar-1-1-12-and-1-2-6-are-now-available)

## 🔹 Docker - Introducing Docker Hardened Images: Secure, Minimal, and Ready for Production
이 기술 블로그 글은 Docker가 새롭게 소개한 'Hardened Images'에 대해 설명합니다. Docker는 개발자들이 소프트웨어를 효율적이고 안전하게 구축, 공유, 실행할 수 있도록 지원해왔으며, Docker Hub는 매달 140억 건 이상의 다운로드를 기록하며 전 세계적으로 소프트웨어 전달을 지원합니다. 이러한 대규모 운영 경험을 바탕으로 Docker는 보안이 강화되고, 최소한의 구성 요소로 제작된 프로덕션 준비 완료 이미지를 제공하게 되었습니다. 이 'Hardened Images'는 개발자들이 안전하고 신뢰할 수 있는 환경에서 작업하도록 돕습니다.
👉 [자세히 보기](https://www.docker.com/blog/introducing-docker-hardened-images/)

## 🔹 Java - Towards a JSON API for the JDK
제목: JDK를 위한 JSON API를 향하여  
요약: 이 글은 JDK를 위한 JSON API 개발에 대한 생각과 계획을 공유하고 있습니다.  
링크: [원문 링크](https://inside.java/2025/05/20/json-api-jdk/)
👉 [자세히 보기](https://inside.java/2025/05/20/json-api-jdk/)

## 🔹 Golang - Go Cryptography Security Audit
제목: Go 암호화 보안 감사  
요약: Go의 암호화 라이브러리가 Trail of Bits에 의해 감사를 받았습니다.
👉 [자세히 보기](https://go.dev/blog/tob-crypto-audit)

## 🔹 Helm - Helm @ KubeCon + CloudNativeCon EU '25
블로그 글 요약: Helm 팀이 2025년 4월 1일부터 4일까지 영국 런던에서 열리는 KubeCon + CloudNativeCon EU에 참가합니다. 이번 행사에서는 올해 말 출시 예정인 Helm 4에 대한 대화를 나눌 수 있는 기회가 주어집니다. 참석자들은 발표 세션과 프로젝트 파빌리온의 Helm 부스에서 유지 관리자들과 소통할 수 있습니다. 행사 기간 동안 진행되는 다양한 Helm 관련 활동에 대한 자세한 내용은 블로그에서 확인할 수 있습니다.
👉 [자세히 보기](https://helm.sh/blog/helm-at-kubecon-eu-25/)

