# 🛠️ 2025-05-30 기술 업데이트 요약

## 🔹 Kubernetes - Kubernetes v1.33: In-Place Pod Resize Graduated to Beta
Kubernetes v1.33에서는 기존에 알파 단계로 도입된 '인플레이스 Pod 리사이즈' 기능이 베타로 승급되었습니다. 이 기능은 실행 중인 Pod의 CPU 및 메모리 요청과 제한을 변경할 수 있도록 하여, 서비스 중단 없이 리소스를 관리할 수 있게 합니다. 이는 특히 상태 저장 애플리케이션이나 장기 실행 작업에 유용하며, 자원 활용을 최적화하고 빠르게 스케일링할 수 있는 장점을 제공합니다. 알파 단계에서 베타로 넘어오면서 사용자 경험을 개선하고 안정성을 향상시켰으며, 사이드카 컨테이너에 대한 지원도 추가되었습니다. 앞으로의 개발 방향은 더 안정적인 프로덕션 환경 지원과 사용자 피드백을 통한 기능 개선에 집중할 예정입니다.
👉 [자세히 보기](https://kubernetes.io/blog/2025/05/16/kubernetes-v1-33-in-place-pod-resize-beta/)

## 🔹 Spring Boot - Spring Cloud 2025.0.0 (aka Northfields) has been released
Spring Cloud 2025.0.0(Northfields) 버전이 정식 출시되었습니다. 이번 릴리스는 Spring Boot 3.5.0과 호환되며, 주요 변경 사항으로는 Spring Cloud Gateway의 새로운 핸들러 지원, Bucket4jRateLimiter 지원, WebClientRouting 인프라의 폐기, 모듈 및 스타터 이름의 변경 등이 포함되어 있습니다. 또한 Spring Cloud Config는 AWS S3 버킷의 YAML 프로파일 문서를 지원하며, Spring Cloud Kubernetes는 새로운 복합 구성 소스로서 Kubernetes를 지원합니다. 이외에도 여러 모듈들이 업데이트되었습니다. 자세한 내용은 GitHub 릴리스 노트를 참고하세요.
👉 [자세히 보기](https://spring.io/blog/2025/05/29/spring-cloud-2025-0-0-is-abvailable)

## 🔹 Docker - Introducing Docker Hardened Images: Secure, Minimal, and Ready for Production
이 기술 블로그 글에서는 Docker에서 제공하는 새로운 'Docker Hardened Images'에 대해 소개하고 있습니다. Docker는 개발자들이 소프트웨어를 효율적이고 안전하게 구축, 공유, 실행할 수 있도록 돕는 데 중점을 두어 왔습니다. 현재 Docker Hub는 전 세계적으로 소프트웨어 제공을 지원하며 매달 14억 개 이상의 이미지와 110억 회 이상의 다운로드를 기록하고 있습니다. 이러한 규모 덕분에 현대 소프트웨어가 어떻게 구축되는지에 대한 독특한 통찰력을 제공할 수 있습니다. Hardened Images는 보안이 강화된 최소한의 이미지로, 프로덕션 환경에서 바로 사용할 수 있도록 설계되었습니다.
👉 [자세히 보기](https://www.docker.com/blog/introducing-docker-hardened-images/)

## 🔹 Java - The Inside Java Newsletter: Java’s 30th Birthday &amp; JavaOne!
이 기술 블로그 글은 2025년 5월의 Inside Java 뉴스레터에 대한 요약입니다. 이번 뉴스레터는 Java의 30번째 생일을 기념하고 JavaOne 2025의 콘텐츠를 소개합니다. 여러 팟캐스트 인터뷰, 커뮤니티 소식, 최신 기술 비디오 등을 통해 Java의 최신 혁신에 대해 개발자들이 업데이트될 수 있도록 돕습니다. 또한 학생과 교사를 위한 Java 학습 전용 새 웹사이트에 대한 내용도 다음 호에서 더 다룰 예정입니다. Inside Java 뉴스레터는 Java 개발자 관계 팀에서 제작하며, Java 플랫폼 그룹의 기술 콘텐츠를 강조합니다. 뉴스레터 아카이브를 확인하고 구독하거나 친구에게 공유할 수 있습니다.
👉 [자세히 보기](https://inside.java/2025/05/28/inside-java-newsletter/)

## 🔹 Golang - Go Cryptography Security Audit
"Go 암호화 보안 감사"라는 제목의 기술 블로그 글은 Go의 암호화 라이브러리가 Trail of Bits에 의해 감사를 받았다는 내용을 다루고 있습니다. 이 감사의 목적은 Go의 암호화 구현의 보안성을 평가하고, 잠재적인 취약점을 식별하여 개선하기 위한 것입니다. Trail of Bits는 보안 감사를 전문으로 하는 회사로, 이번 감사를 통해 Go의 암호화 라이브러리가 안전하게 설계되고 구현되었음을 확인했습니다.
👉 [자세히 보기](https://go.dev/blog/tob-crypto-audit)

## 🔹 Helm - Helm @ KubeCon + CloudNativeCon EU '25
블로그 글 요약: 헬름 팀이 2025년 4월 1일부터 4일까지 영국 런던에서 열리는 KubeCon + CloudNativeCon EU '25에 참석합니다. 헬름 4가 올해 말 출시될 예정이므로 헬름 유지관리자들과의 대화에 참여하고, 헬름 부스와 발표 세션에서 자세한 정보를 얻을 수 있습니다. 주간 동안 진행되는 헬름 관련 활동에 대한 자세한 내용은 링크를 참조하세요.
👉 [자세히 보기](https://helm.sh/blog/helm-at-kubecon-eu-25/)

