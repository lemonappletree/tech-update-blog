# 🛠️ 2025-06-01 기술 업데이트 요약

## 🔹 Kubernetes - Kubernetes v1.33: In-Place Pod Resize Graduated to Beta
Kubernetes 프로젝트 팀은 Kubernetes v1.27에서 알파 버전으로 처음 도입된 '인플레이스 Pod 리사이즈' 기능이 v1.33에서 베타 버전으로 승격되어 기본적으로 활성화된다고 발표했습니다. 이 기능은 Kubernetes 워크로드의 자원 관리를 더 유연하고 덜 방해적으로 만드는 중요한 이정표입니다. 인플레이스 Pod 리사이즈는 실행 중인 Pod의 CPU와 메모리 자원을 재시작 없이 조정할 수 있게 해줍니다. 이는 상태 저장 서비스, 배치 작업, 재시작에 민감한 워크로드에 유리합니다. 알파에서 베타로 넘어오면서 기능의 안정성과 사용자 경험이 개선되었습니다. 앞으로 이 기능의 안정성을 강화하고, 사용자의 피드백을 받아 추가 개선을 진행할 예정입니다. 이 기능은 이제 Kubernetes v1.33 클러스터에서 기본적으로 사용 가능합니다.
👉 [자세히 보기](https://kubernetes.io/blog/2025/05/16/kubernetes-v1-33-in-place-pod-resize-beta/)

## 🔹 Spring Boot - Spring Cloud 2025.0.0 (aka Northfields) has been released
Spring Cloud 2025.0.0 버전이 공식적으로 출시되었습니다. 이 버전은 Spring Boot 3.5.0과 호환되며, 주요 변경 사항은 다음과 같습니다. 

Spring Cloud Gateway는 spring-cloud-function 및 spring-cloud-stream 핸들러 지원을 추가하였고, 새로운 모듈 및 시작자 이름을 도입하였습니다. 또한, WebClientRouting 인프라가 폐기될 예정입니다. 

Spring Cloud Config는 AWS S3 버킷에서 YAML 프로파일 문서 지원을 추가하였으며, Spring Cloud Kubernetes는 구성 소스로 Kubernetes를 통합하였습니다. Spring Cloud Circuitbreaker는 반응형 벌크헤드 지원을 추가하였고, Spring Cloud Netflix는 Apache HTTP Client 5의 RequestConfig를 사용자 정의할 수 있게 하였습니다.

각 모듈은 2025.0.0 버전으로 업데이트되었으며, 자세한 내용은 GitHub, Gitter, Stack Overflow에서 확인할 수 있습니다. Maven과 Gradle을 사용하여 프로젝트에 Spring Cloud 2025.0.0을 통합할 수 있습니다.
👉 [자세히 보기](https://spring.io/blog/2025/05/29/spring-cloud-2025-0-0-is-abvailable)

## 🔹 Docker - Introducing Docker Hardened Images: Secure, Minimal, and Ready for Production
이 기술 블로그 글은 Docker의 새로운 강화 이미지를 소개하는 내용입니다. Docker는 개발자들이 소프트웨어를 효율적이고 안전하게 구축, 공유 및 실행할 수 있도록 돕는 데 초점을 맞추고 있습니다. Docker Hub는 매달 140억 번 이상의 다운로드와 1,400만 개 이상의 이미지를 통해 글로벌 소프트웨어 전달을 지원하고 있습니다. 이러한 규모 덕분에 현대 소프트웨어가 어떻게 구축되는지에 대한 독특한 통찰력을 제공할 수 있습니다. 새로운 Docker 강화 이미지는 보안이 강화되고, 최소화된 구성을 제공하며, 프로덕션 환경에 바로 사용할 수 있도록 설계되었습니다.
👉 [자세히 보기](https://www.docker.com/blog/introducing-docker-hardened-images/)

## 🔹 Java - The Inside Java Newsletter: Java’s 30th Birthday &amp; JavaOne!
2025년 5월의 Inside Java 뉴스레터는 Java의 30번째 생일을 기념하며 JavaOne 2025에서의 콘텐츠를 소개합니다. 이번 호에서는 여러 팟캐스트 인터뷰, 커뮤니티 소식, 그리고 최신 기술 동영상을 통해 개발자들이 Java의 최신 혁신을 따라갈 수 있도록 돕습니다. 또한 학생과 교사를 위한 Java 학습 전용 웹사이트에 대한 소식을 다가오는 호에서 더 다룰 예정입니다. Inside Java 뉴스레터는 Java 개발자 관계 팀에 의해 제작되며, Java 플랫폼 그룹의 기술 콘텐츠를 강조합니다. 뉴스레터 아카이브를 확인하고, 구독하며 친구에게 공유해보세요!
👉 [자세히 보기](https://inside.java/2025/05/28/inside-java-newsletter/)

## 🔹 Golang - Go Cryptography Security Audit
제목: Go 암호화 보안 감사  
요약: Go의 암호화 라이브러리가 Trail of Bits에 의해 감사를 받았습니다.  
링크: https://go.dev/blog/tob-crypto-audit
👉 [자세히 보기](https://go.dev/blog/tob-crypto-audit)

## 🔹 Helm - Helm @ KubeCon + CloudNativeCon EU '25
제목: Helm @ KubeCon + CloudNativeCon EU '25

요약: Helm 팀이 2025년 4월 1일부터 4일까지 영국 런던에서 열리는 KubeCon + CloudNativeCon EU에 참가합니다. 올해 말 출시 예정인 Helm 4에 대한 논의에 참여할 수 있는 기회가 주어지며, 세션 발표와 프로젝트 파빌리온 내 Helm 부스를 통해 유지보수자들과 소통할 수 있습니다. 주간 동안 진행되는 Helm 관련 활동에 대한 자세한 정보는 링크를 참고하세요.
👉 [자세히 보기](https://helm.sh/blog/helm-at-kubecon-eu-25/)

