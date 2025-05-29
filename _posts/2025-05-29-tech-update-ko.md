# 🛠️ 2025-05-29 기술 업데이트 요약

## 🔹 Kubernetes - Kubernetes v1.33: In-Place Pod Resize Graduated to Beta
Kubernetes v1.33 릴리스에서 인플레이스 Pod 리사이즈 기능이 베타로 승격되었습니다. 이 기능은 Kubernetes v1.27에서 처음 알파 버전으로 소개되었으며, 이제 기본적으로 활성화됩니다. 인플레이스 Pod 리사이즈는 실행 중인 Pod 내에서 CPU 및 메모리 자원을 재할당할 수 있어, 상태 저장 서비스나 배치 작업 등 재시작에 민감한 워크로드에 대한 중단을 줄여줍니다. 또한 클러스터 자원 활용을 개선하고, 수직적 스케일링을 보다 빠르게 처리할 수 있도록 돕습니다. 베타 버전에서는 리사이즈 서브리소스를 통한 자원 변경을 지원하며, 여러 안정성 및 신뢰성 개선이 이루어졌습니다. 앞으로 생산 환경에서의 안정성 강화, 제한 사항 해결, VerticalPodAutoscaler와의 통합 등이 예정되어 있습니다. 사용자는 피드백을 제공하여 기능 향상에 기여할 수 있습니다.
👉 [자세히 보기](https://kubernetes.io/blog/2025/05/16/kubernetes-v1-33-in-place-pod-resize-beta/)

## 🔹 Spring Boot - Spring Modulith 1.4 GA, 1.3.6, and 1.2.13 released
블로그 글에서는 Spring Modulith 1.4 GA가 발표되었으며, 새로운 기능과 향상된 점들에 대해 설명하고 있습니다. 핵심 기능으로는 `ApplicationModule(s)` 추상화 및 문서 생성의 개선, `NamedInterfaces`를 프로그래밍적으로 감지하기 위한 SPI 도입, `JavaPackage`의 성능 저하 문제 해결 등이 포함됩니다. 통합 테스트에서는 `@ApplicationModuleTest`를 통해 테스트 소스에 선언된 클래스의 빈 인스턴스를 사용할 수 있게 되었고, 이벤트 퍼블리케이션 인프라가 성능 개선 및 구조적으로 동일한 이벤트 지원을 위해 개편되었습니다. 실행 시간 및 관찰 가능성 지원도 개선되어 모듈의 안정적인 순서 보장 및 더욱 세밀한 메트릭 통합이 가능해졌습니다. 또한, 최신 Spring Boot 3.5 및 Framework 6.2로의 업그레이드가 이루어졌으며, 2.0 주요 릴리스 준비가 진행 중입니다. IntelliJ의 지원도 곧 제공될 예정입니다.
👉 [자세히 보기](https://spring.io/blog/2025/05/28/spring-modulith-1-4-1-3-6-and-1-2-13-released)

## 🔹 Docker - Introducing Docker Hardened Images: Secure, Minimal, and Ready for Production
이 블로그 글에서는 Docker가 새롭게 선보이는 강화된 이미지를 소개합니다. Docker는 개발자가 소프트웨어를 효율적이고 안전하게 구축, 공유, 실행할 수 있도록 지원하는 데 중점을 두어 왔습니다. 현재 Docker Hub는 매월 14억 개 이상의 이미지와 110억 건 이상의 다운로드를 통해 글로벌 소프트웨어 전달을 지원하고 있습니다. 이러한 규모는 현대 소프트웨어 구축 방법에 대한 독특한 관점을 제공하며, 이번에 발표된 강화된 이미지는 이러한 통찰을 바탕으로 보안성과 최소화를 중점으로 하여 프로덕션 환경에 바로 사용할 수 있도록 설계되었습니다.
👉 [자세히 보기](https://www.docker.com/blog/introducing-docker-hardened-images/)

## 🔹 Java - The Inside Java Newsletter: Java’s 30th Birthday &amp; JavaOne!
블로그 글 요약: "The Inside Java Newsletter" 2025년 5월호는 자바의 30번째 생일을 기념하고 JavaOne 2025의 콘텐츠를 소개합니다. 이번 호에서는 여러 팟캐스트 인터뷰, 커뮤니티 소식, 최신 기술 동영상 등을 통해 개발자들이 자바의 최신 혁신을 따라잡을 수 있도록 돕습니다. 또한, 학생과 교사를 위한 자바 학습 전용 새 웹사이트에 대한 소식도 곧 전할 예정입니다. 이 뉴스레터는 Java Developer Relations 팀에서 제작하며, Java Platform Group의 기술 콘텐츠를 강조합니다. 아카이브를 확인하고 구독하여 친구에게 공유해보세요!
👉 [자세히 보기](https://inside.java/2025/05/28/inside-java-newsletter/)

## 🔹 Golang - Go Cryptography Security Audit
"Go Cryptography Security Audit"라는 제목의 기술 블로그 글에서는 Go 언어의 암호화 라이브러리가 Trail of Bits에 의해 보안 감사가 이루어졌다는 내용을 다루고 있습니다. 이 감사는 Go의 암호화 라이브러리의 안전성과 신뢰성을 평가하고 개선하기 위한 목적으로 진행되었습니다.
👉 [자세히 보기](https://go.dev/blog/tob-crypto-audit)

## 🔹 Helm - Helm @ KubeCon + CloudNativeCon EU '25
제목: Helm @ KubeCon + CloudNativeCon EU '25

Helm 팀이 2025년 4월 1일부터 4일까지 영국 런던에서 열리는 KubeCon + CloudNativeCon EU에 참가합니다. 올해 말 출시 예정인 Helm 4에 관한 대화에 참여하고 싶다면, 토크 세션과 프로젝트 파빌리온의 Helm 부스를 방문해 보세요. 일주일 동안 진행되는 Helm 관련 활동에 대한 자세한 내용은 링크를 참고하세요.
👉 [자세히 보기](https://helm.sh/blog/helm-at-kubecon-eu-25/)

