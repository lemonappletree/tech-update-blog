# 🛠️ 2025-05-23 기술 업데이트 요약

## 🔹 Kubernetes - Kubernetes v1.33: In-Place Pod Resize Graduated to Beta
Kubernetes 프로젝트는 v1.33 릴리스에서 "인플레이스 Pod 리사이즈" 기능이 베타로 승격되었음을 발표했습니다. 이 기능은 Kubernetes v1.27에서 알파로 처음 소개되었으며, 리소스 관리의 유연성을 높이고 중단을 줄이는 데 중요한 역할을 합니다. 전통적으로 컨테이너에 할당된 CPU나 메모리 리소스를 변경하려면 Pod를 재시작해야 했지만, 인플레이스 리사이징은 실행 중인 Pod 내에서 이러한 리소스를 변경할 수 있도록 합니다. 이는 상태를 유지해야 하는 애플리케이션이나 배치 작업, 재시작에 민감한 작업에 특히 유용합니다.

이번 베타 버전에서는 사용자 경험 개선, 안정성 향상, 사이드카 컨테이너 지원 등이 추가되었습니다. 향후에는 기능 강화와 VerticalPodAutoscaler 통합 등이 계획되어 있습니다. 이 기능은 v1.33부터 기본적으로 활성화되어 있으며, 사용자는 Kubernetes 문서를 통해 더 자세한 정보를 얻고 피드백을 제공할 수 있습니다.
👉 [자세히 보기](https://kubernetes.io/blog/2025/05/16/kubernetes-v1-33-in-place-pod-resize-beta/)

## 🔹 Spring Boot - Spring for Apache Pulsar 1.1.12 and 1.2.6 are now available
제목: Spring for Apache Pulsar 1.1.12 및 1.2.6 출시

요약: 팀과 기여자들을 대신하여, Spring for Apache Pulsar의 버전 1.1.12와 1.2.6이 출시되어 이제 Maven Central에서 사용할 수 있게 되었다고 발표했습니다. 이 릴리스들은 곧 출시될 Spring Boot 3.3.12와 3.4.6에 각각 포함될 예정입니다. 자세한 내용은 릴리스 노트(1.1.12 및 1.2.6)를 참조하세요.
👉 [자세히 보기](https://spring.io/blog/2025/05/23/spring-for-apache-pulsar-1-1-12-and-1-2-6-are-now-available)

## 🔹 Docker - Introducing Docker Hardened Images: Secure, Minimal, and Ready for Production
Docker는 처음부터 개발자가 소프트웨어를 효율적이고 안전하게 구축, 공유 및 실행할 수 있도록 지원하는 데 중점을 두었습니다. 현재 Docker Hub는 매달 14억 개 이상의 이미지와 110억 이상의 다운로드를 지원하며, 이를 통해 현대 소프트웨어가 어떻게 구축되는지에 대한 독특한 시각을 제공합니다. 새로운 Docker 강화 이미지는 이러한 경험을 바탕으로 보안과 최소화를 중점으로 하고 있으며, 프로덕션 환경에 즉시 사용 가능한 상태로 제공됩니다.
👉 [자세히 보기](https://www.docker.com/blog/introducing-docker-hardened-images/)

## 🔹 Java - Towards a JSON API for the JDK
**블로그 요약:**  
이 블로그 글은 JDK(자바 개발 키트)를 위한 JSON API 개발에 대한 생각과 계획을 공유합니다. JSON API는 데이터 교환을 위한 표준 형식인 JSON을 처리하기 위한 API로, JDK에 통합되면 개발자들이 JSON 데이터를 보다 쉽게 다룰 수 있게 될 것입니다.
👉 [자세히 보기](https://inside.java/2025/05/20/json-api-jdk/)

## 🔹 Golang - Go Cryptography Security Audit
제목: Go 암호화 보안 감사  
요약: Trail of Bits에서 Go의 암호화 라이브러리에 대한 감사를 진행했습니다.  
링크: https://go.dev/blog/tob-crypto-audit
👉 [자세히 보기](https://go.dev/blog/tob-crypto-audit)

## 🔹 Helm - Helm @ KubeCon + CloudNativeCon EU '25
제목: Helm @ KubeCon + CloudNativeCon EU '25

요약: Helm 팀이 2025년 4월 1일부터 4일까지 영국 런던에서 열리는 KubeCon + CloudNativeCon EU '25에 참여합니다. 올해 말 출시 예정인 Helm 4에 대한 대화에 참여할 수 있는 기회입니다. 프로젝트 파빌리온에 있는 Helm 부스에서 유지 관리자들과 함께하는 토크 세션에 참석해 보세요. 주간 동안 진행되는 모든 Helm 관련 활동에 대한 자세한 내용은 링크를 통해 확인할 수 있습니다.
👉 [자세히 보기](https://helm.sh/blog/helm-at-kubecon-eu-25/)

