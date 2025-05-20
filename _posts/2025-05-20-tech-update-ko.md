# 🛠️ 2025-05-20 기술 업데이트 요약

## 🔹 Kubernetes - Kubernetes v1.33: In-Place Pod Resize Graduated to Beta
이 기술 블로그는 쿠버네티스 v1.33에서 "인-플레이스 Pod 리사이즈" 기능이 알파 버전에서 베타 버전으로 승격되었음을 알립니다. 이 기능은 CPU 및 메모리 리소스를 할당하기 위해 Pod를 재시작해야 했던 기존 방식과 달리, 실행 중인 Pod의 리소스를 재시작 없이 변경할 수 있도록 합니다. 이는 상태 저장 애플리케이션이나 민감한 작업에 있어 중단을 줄이고 리소스 활용을 개선하는 데 도움을 줍니다.

베타 버전으로의 승격은 사용 편의성 개선과 안정성 향상을 포함하며, Pod 리소스를 조정하는 새로운 `resize` 서브리소스를 도입했습니다. 또한, 사이드카 컨테이너에 대한 지원과 리소스 할당 관리의 개선 등 여러 안정성과 신뢰성 향상이 이루어졌습니다.

커뮤니티는 기능의 안정성과 성능을 계속해서 개선하고, 수직 포드 오토스케일러(VPA)와의 통합을 추진할 예정입니다. 사용자의 피드백은 이 기능을 더욱 발전시키는 데 중요한 역할을 합니다.
👉 [자세히 보기](https://kubernetes.io/blog/2025/05/16/kubernetes-v1-33-in-place-pod-resize-beta/)

## 🔹 Spring Boot - Spring Security 6.3.10 Released
제목: Spring Security 6.3.10 출시

요약: 팀과 기여한 모든 사람들을 대표하여 Spring Security 6.3.10의 출시를 발표하게 되어 기쁩니다. 자세한 내용은 변경 로그를 확인하세요. 프로젝트 페이지, GitHub, 이슈 페이지, 문서에 대한 링크도 제공됩니다.
👉 [자세히 보기](https://spring.io/blog/2025/05/19/spring-security-6-3-10)

## 🔹 Docker - Introducing Docker Hardened Images: Secure, Minimal, and Ready for Production
이 블로그 글은 Docker의 새로운 기능인 Hardened Images를 소개합니다. Docker는 개발자들이 소프트웨어를 효율적이고 안전하게 구축, 공유, 실행할 수 있도록 돕는 데 중점을 두고 있으며, 현재 Docker Hub는 매월 14억 개 이상의 이미지와 110억 번 이상의 다운로드를 처리하고 있습니다. 이러한 규모 덕분에 Docker는 현대 소프트웨어가 어떻게 구축되는지에 대한 독특한 인사이트를 제공합니다. Hardened Images는 보안이 강화된 최소한의 이미지로, 프로덕션 환경에서 바로 사용할 수 있도록 설계되었습니다.
👉 [자세히 보기](https://www.docker.com/blog/introducing-docker-hardened-images/)

## 🔹 Java - JEP targeted to JDK 25: 513: Flexible Constructor Bodies
제목이 "JEP 513: 유연한 생성자 본문"인 기술 블로그 글은 JDK 25에 목표를 두고 있는 JEP 513에 관한 내용입니다. 이 JEP는 생성자 본문을 보다 유연하게 작성할 수 있도록 개선하는 내용을 다루고 있습니다. 더 자세한 내용은 제공된 링크를 통해 확인할 수 있습니다.
👉 [자세히 보기](https://inside.java/2025/05/19/jep513-target-jdk25/)

## 🔹 Golang - Go Cryptography Security Audit
제목: Go 암호화 보안 감사

요약: Go의 암호화 라이브러리가 Trail of Bits에 의해 보안 감사를 받았습니다.
👉 [자세히 보기](https://go.dev/blog/tob-crypto-audit)

## 🔹 Helm - Helm @ KubeCon + CloudNativeCon EU '25
이 기술 블로그 글은 Helm 팀이 2025년 4월 1일부터 4일까지 영국 런던에서 열리는 KubeCon + CloudNativeCon EU에 참가한다는 내용을 다루고 있습니다. 올해 말 출시 예정인 Helm 4에 대한 논의를 위해, 참석자들은 Helm 유지보수 팀과 대화할 수 있는 기회를 갖게 됩니다. 행사 기간 동안 Helm 부스와 발표 세션에서 다양한 활동이 진행될 예정입니다. 더 자세한 정보는 블로그에서 확인할 수 있습니다.
👉 [자세히 보기](https://helm.sh/blog/helm-at-kubecon-eu-25/)

