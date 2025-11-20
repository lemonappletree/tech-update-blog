# 🛠️ 2025-11-20 기술 업데이트 요약

## 🔹 Kubernetes - Ingress NGINX Retirement: What You Need to Know
Ingress NGINX의 은퇴가 발표되었습니다. Kubernetes SIG Network와 보안 대응 위원회는 2026년 3월까지 Ingress NGINX의 유지보수를 지속하겠지만, 그 이후에는 더 이상 릴리스, 버그 수정 또는 보안 취약점 해결이 이루어지지 않을 것입니다. 기존 배포는 계속 작동하며 설치 아티팩트는 계속 이용 가능합니다. 사용자는 Gateway API로의 마이그레이션을 고려하거나 다른 Ingress 컨트롤러로 전환하는 것이 권장됩니다. Ingress NGINX는 Kubernetes 프로젝트 초기에 개발된 컨트롤러로, 유연성과 풍부한 기능 덕분에 인기를 끌었습니다. 하지만 유지보수 인력 부족과 기술적 부채로 인해 프로젝트가 종료됩니다. 사용자는 즉시 Gateway API 또는 다른 Ingress 컨트롤러로의 전환을 시작해야 합니다.
👉 [자세히 보기](https://kubernetes.io/blog/2025/11/11/ingress-nginx-retirement/)

## 🔹 Spring Boot - Spring Batch 6.0.0 GA is out!
Spring Batch 6.0.0 GA 버전이 출시되었습니다. 이번 주요 릴리스는 Spring Framework 7.0을 기반으로 하며, Spring Boot 4.0을 통해 제공됩니다. 새로운 버전에서는 최신 Spring 종속성 업그레이드, JSpecify를 통한 포괄적인 null 안전성, 향상된 청크 지향 처리 모델, 향상된 동시성 모델 등이 포함되어 있습니다. 또한, 로컬 데이터 청킹 및 원격 단계 실행 지원, SEDA 스타일 메시지 채널, 우아한 종료 및 실패한 작업 실행 복구 기능, Java Flight Recorder를 통한 관측 가능 이벤트 지원 등이 추가되었습니다. 자세한 내용은 공식 문서와 릴리스 노트를 참조하세요. 많은 기여자들에게 감사의 인사를 전하며, 여러분의 피드백이 이번 릴리스를 완성하는 데 큰 도움이 되었습니다.
👉 [자세히 보기](https://spring.io/blog/2025/11/19/spring-batch-6-0-0-ga)

## 🔹 Docker - Why I joined Docker: security at the center of the software supply chain
도커의 CISO인 마크 레크너는 도커가 소프트웨어 공급망을 강화할 뿐만 아니라 이를 적극적으로 보호하는 미래 비전을 공유합니다. 사이버 보안은 이제 전환점을 맞이했으며, 가장 큰 위협은 더 이상 개별 시스템을 공격하지 않고 시스템 간의 연결을 통해 이동합니다. 현대의 공격 표면은 모든 의존성, 모든 컨테이너 등을 포함합니다.
👉 [자세히 보기](https://www.docker.com/blog/why-i-joined-docker-security-at-the-center-of-the-software-supply-chain/)

## 🔹 Java - JEP targeted to JDK 26: 524: PEM Encodings of Cryptographic Objects (Second Preview)
이 기술 블로그 글에서는 JDK 26에 목표로 한 JEP 524에 대해 다루고 있습니다. 이 JEP는 암호화 객체의 PEM 인코딩을 두 번째로 미리보기하는 내용입니다. 이는 PEM 형식의 암호화 객체 지원을 개선하려는 노력의 일환으로, JDK 26에 포함될 예정입니다.
👉 [자세히 보기](https://inside.java/2025/11/17/jep524-target-jdk26/)

## 🔹 Golang - Go’s Sweet 16
블로그 글 "Go’s Sweet 16"은 프로그래밍 언어 Go의 16번째 생일을 기념하는 내용입니다. 글에서는 Go 언어가 지난 16년 동안 어떻게 발전해왔는지, 주요 특징과 장점, 그리고 커뮤니티의 성장을 강조하고 있습니다. Go 언어의 간결함과 효율성, 그리고 다양한 분야에서의 적용 사례가 언급되며, 앞으로의 발전 방향에 대해서도 간략히 다루고 있습니다.
👉 [자세히 보기](https://go.dev/blog/16years)

