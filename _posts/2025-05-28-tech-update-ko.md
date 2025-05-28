# 🛠️ 2025-05-28 기술 업데이트 요약

## 🔹 Kubernetes - Kubernetes v1.33: In-Place Pod Resize Graduated to Beta
Kubernetes v1.33에서 인플레이스(In-Place) Pod 리사이즈 기능이 베타 버전으로 업데이트되었습니다. 이 기능은 Kubernetes v1.27에서 알파 버전으로 처음 도입되었으며, 이제 기본적으로 활성화됩니다. 인플레이스 Pod 리사이즈는 실행 중인 Pod의 CPU와 메모리 요청 및 제한을 변경할 수 있게 하여, 전통적으로 Pod를 재시작해야 했던 과정을 생략할 수 있습니다. 이는 상태 저장 애플리케이션이나 배치 작업 등에서 발생할 수 있는 중단을 줄이고, 리소스 활용도를 높이며, 더 빠른 스케일링을 가능하게 합니다. 알파에서 베타로 전환되면서 사용자 경험 및 안정성이 개선되었고, 사이드카 컨테이너에 대한 지원도 추가되었습니다. 향후 개발 목표로는 기능의 안정성 강화 및 VerticalPodAutoscaler와의 통합 등이 있습니다. Kubernetes v1.33 클러스터에서 이 기능을 실험해 볼 수 있으며, 사용자 피드백이 중요합니다.
👉 [자세히 보기](https://kubernetes.io/blog/2025/05/16/kubernetes-v1-33-in-place-pod-resize-beta/)

## 🔹 Spring Boot - This Week in Spring (AI) - May 27th, 2025
이번 주 "This Week in Spring" 블로그에서는 저자가 다양한 행사와 발표를 통해 바쁜 한 주를 보낸 이야기를 전하고 있습니다. 스톡홀름의 JForum 이벤트와 바르셀로나의 Spring I/O 이벤트 등에서 Spring AI에 대한 발표와 키노트가 있었고, 여러 공동 발표도 진행했습니다. 또한, 여러 도시를 방문하며 고객들과 만났으며, 다양한 컨퍼런스에도 참가했습니다.

이번 주의 주요 소식으로는 Spring AI 1.0 출시가 있습니다. 이 릴리스는 수년간 준비된 결과물로, 다양한 모듈이 채팅 모델, 이미지 모델, 전사(轉寫) 모델, 임베딩 모델, 벡터 저장소를 지원합니다. Microsoft Azure, AWS, Google, Elastic, Redis, MongoDB, Oracle 등 여러 기업들이 Spring AI 1.0에 대한 글을 게시하며 관심을 보였습니다.

그 외에도 Spring Data AOT 리포지토리 지원, Spring Integration 6.5 GA, Spring Boot의 여러 버전 업데이트 소식이 있으며, 다양한 블로그 글과 비디오도 소개되었습니다. 이러한 모든 내용은 활발한 커뮤니티 덕분에 가능했다고 강조하며, 커뮤니티에 감사를 표하고 있습니다.
👉 [자세히 보기](https://spring.io/blog/2025/05/27/this-week-in-spring-may-27th-2025)

## 🔹 Docker - Introducing Docker Hardened Images: Secure, Minimal, and Ready for Production
이 블로그 글은 Docker의 새로운 기능인 "Docker Hardened Images"에 대해 소개하고 있습니다. Docker는 개발자들이 소프트웨어를 효율적이고 안전하게 구축, 공유, 실행할 수 있도록 돕는 것을 목표로 하고 있으며, Docker Hub는 매달 140억 회 이상의 다운로드와 함께 전 세계적으로 소프트웨어 배포를 지원하고 있습니다. 이러한 대규모 운영을 통해 현대 소프트웨어가 어떻게 구축되는지에 대한 독특한 관점을 제공하고 있습니다. 이 글에서는 Docker Hardened Images가 프로덕션 환경에서 안전하고 최소화된 이미지를 제공함으로써 소프트웨어의 보안을 강화하는 방법에 대해 설명하고 있습니다.
👉 [자세히 보기](https://www.docker.com/blog/introducing-docker-hardened-images/)

## 🔹 Java - JEP targeted to JDK 25: 510: Key Derivation Function API
제목이 "JEP targeted to JDK 25: 510: Key Derivation Function API"인 기술 블로그 글은 JDK 25를 목표로 하는 JEP 510에 대한 내용을 다루고 있습니다. 이 JEP는 키 파생 함수(API)를 소개하고 있으며, 해당 API는 보안 관련 작업에 사용될 수 있는 기능을 제공합니다. 더 자세한 내용은 원문 링크를 통해 확인할 수 있습니다.
👉 [자세히 보기](https://inside.java/2025/05/26/jep510-target-jdk25/)

## 🔹 Golang - Go Cryptography Security Audit
제목: Go 암호화 보안 감사  
요약: Go의 암호화 라이브러리가 Trail of Bits에 의해 감사를 받았습니다.  
링크: [Go Cryptography Security Audit](https://go.dev/blog/tob-crypto-audit)  

이 글은 Go 프로그래밍 언어의 암호화 라이브러리에 대한 보안 감사에 관한 내용을 다루고 있습니다. Trail of Bits라는 보안 전문 회사가 Go의 암호화 라이브러리를 평가하여 보안성을 점검하고 개선점을 제시했습니다. 이번 감사는 Go 사용자에게 더 안전한 환경을 제공하기 위한 노력의 일환입니다.
👉 [자세히 보기](https://go.dev/blog/tob-crypto-audit)

## 🔹 Helm - Helm @ KubeCon + CloudNativeCon EU '25
제목: KubeCon + CloudNativeCon EU '25에서의 Helm

Helm 팀이 4월 1일부터 4일까지 영국 런던에서 열리는 KubeCon + CloudNativeCon EU '25에 참가합니다. 올해 말 출시 예정인 Helm 4에 대한 논의를 위해 발표 세션과 Helm 부스에서 유지보수팀과의 대화에 참여할 수 있습니다. 주간 동안의 Helm 관련 활동에 대한 자세한 내용은 링크를 참조하세요.
👉 [자세히 보기](https://helm.sh/blog/helm-at-kubecon-eu-25/)

