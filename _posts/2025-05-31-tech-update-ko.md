# 🛠️ 2025-05-31 기술 업데이트 요약

## 🔹 Kubernetes - Kubernetes v1.33: In-Place Pod Resize Graduated to Beta
블로그 글은 Kubernetes 프로젝트가 v1.33 버전에서 '인-플레이스 Pod 리사이즈' 기능을 알파에서 베타로 업데이트하고 기본적으로 활성화한다고 발표하는 내용입니다. 이 기능은 컨테이너의 CPU 및 메모리 자원을 Pod를 재시작하지 않고도 조정할 수 있게 해주며, 이는 유상성 서비스, 배치 작업 및 재시작에 민감한 작업에 유용합니다. Kubernetes의 수직적 확장을 용이하게 하여 자원 사용률을 개선하고, 중단 없이 빠르게 자원을 조정할 수 있게 합니다. 베타 버전으로의 업그레이드에서 사용자가 직접 조작할 수 있는 'resize' 서브리소스를 도입하고, 리사이즈 상태를 Pod 조건을 통해 확인할 수 있게 하는 등 여러 개선이 이루어졌습니다. 앞으로는 기능의 안정성 강화와 VerticalPodAutoscaler와의 통합이 예정되어 있습니다. 사용자는 피드백을 통해 기능 발전에 기여할 수 있습니다.
👉 [자세히 보기](https://kubernetes.io/blog/2025/05/16/kubernetes-v1-33-in-place-pod-resize-beta/)

## 🔹 Spring Boot - Spring Cloud 2025.0.0 (aka Northfields) has been released
Spring Cloud 2025.0.0 버전이 출시되었습니다. 이 버전은 Spring Boot 3.5.0과 호환됩니다. 주요 변경 사항으로는 Spring Cloud Gateway의 모듈 및 스타터 이름 변경, 새로운 모듈 이름에 맞춘 프로퍼티 접두사 변경, 기본적으로 비활성화된 `X-Forwarded-*` 및 `Forwarded` 헤더 기능 등이 있습니다. 또한, Spring Cloud Config는 AWS S3 버킷에서 YAML 프로파일 문서를 지원하며, Spring Cloud Kubernetes는 복합 구성 소스로 Kubernetes를 지원합니다. 각 모듈의 상세한 변경 사항은 GitHub 릴리스 노트에서 확인할 수 있습니다. Maven과 Gradle을 사용하여 프로젝트에 Spring Cloud 2025.0.0을 추가할 수 있습니다.
👉 [자세히 보기](https://spring.io/blog/2025/05/29/spring-cloud-2025-0-0-is-abvailable)

## 🔹 Docker - Introducing Docker Hardened Images: Secure, Minimal, and Ready for Production
이 블로그 글에서는 Docker가 새롭게 소개한 'Docker Hardened Images'에 대해 설명합니다. Docker는 개발자들이 소프트웨어를 효율적이고 안전하게 구축, 공유, 실행할 수 있도록 지원해왔으며, Docker Hub는 매월 110억 건 이상의 이미지 다운로드를 통해 전 세계 소프트웨어 배포를 지원하고 있습니다. 이러한 대규모 운영 경험을 바탕으로 Docker는 보안성과 최소한의 크기를 갖춘 프로덕션 준비 완료 이미지를 제공하여 현대 소프트웨어 개발의 새로운 기준을 제시하고자 합니다.
👉 [자세히 보기](https://www.docker.com/blog/introducing-docker-hardened-images/)

## 🔹 Java - The Inside Java Newsletter: Java’s 30th Birthday &amp; JavaOne!
이 기술 블로그 글은 2025년 5월호 Inside Java 뉴스레터에 대한 요약입니다. 이번 호에서는 Java의 30번째 생일을 기념하고 JavaOne 2025의 콘텐츠를 소개합니다. 여러 팟캐스트 인터뷰, 커뮤니티의 최신 소식, 개발자들이 최신 Java 혁신에 대해 업데이트할 수 있도록 돕는 기술 비디오도 포함되어 있습니다. 학생과 교사를 위한 Java 학습 전용 웹사이트에 대한 정보도 곧 추가될 예정입니다. 이 뉴스레터는 Java 개발자 관계 팀에서 제작하며 Java 플랫폼 그룹의 기술 콘텐츠를 강조합니다. 아카이브를 확인하고, 구독하며 친구에게 공유할 수 있습니다.
👉 [자세히 보기](https://inside.java/2025/05/28/inside-java-newsletter/)

## 🔹 Golang - Go Cryptography Security Audit
제목: Go 암호화 보안 감사  
요약: Go의 암호화 라이브러리가 Trail of Bits에 의해 보안 감사를 받았습니다.
👉 [자세히 보기](https://go.dev/blog/tob-crypto-audit)

## 🔹 Helm - Helm @ KubeCon + CloudNativeCon EU '25
글은 Helm 팀이 2025년 4월 1일부터 4일까지 영국 런던에서 열리는 KubeCon + CloudNativeCon EU에 참가한다는 내용을 담고 있습니다. Helm 4의 출시가 올해 예정되어 있어, 행사 기간 중 진행되는 발표 세션과 Helm 부스에서 유지 관리자들과의 대화에 참여할 수 있습니다. 행사 주간 동안 진행되는 모든 Helm 관련 활동에 대한 자세한 내용은 블로그 글에서 확인할 수 있습니다.
👉 [자세히 보기](https://helm.sh/blog/helm-at-kubecon-eu-25/)

