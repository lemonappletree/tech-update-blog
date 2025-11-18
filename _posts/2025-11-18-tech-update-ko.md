# 🛠️ 2025-11-18 기술 업데이트 요약

## 🔹 Kubernetes - Ingress NGINX Retirement: What You Need to Know
이 글은 Kubernetes SIG Network와 Security Response Committee가 Ingress NGINX의 은퇴 계획을 발표한 내용을 요약한 것입니다. Ingress NGINX는 2026년 3월까지 유지 관리되며, 이후에는 릴리스나 버그 수정, 보안 취약점 해결이 중단됩니다. 기존 배포는 계속 작동할 것이며 설치 아티팩트도 여전히 사용 가능합니다. 사용자는 Gateway API와 같은 대안으로의 전환을 권장합니다. Ingress NGINX는 Kubernetes 프로젝트 초기에 개발된 인그레스 컨트롤러로, 유연성과 다양한 기능 덕분에 많은 인기를 끌었습니다. 그러나 유지 관리의 어려움과 보안 문제로 인해 프로젝트가 종료됩니다. 사용자는 클러스터 관리자 권한으로 `kubectl get pods --all-namespaces --selector app.kubernetes.io/name=ingress-nginx` 명령어를 사용해 Ingress NGINX 사용 여부를 확인할 수 있습니다. 모든 사용자는 가능한 빨리 Gateway API나 다른 인그레스 컨트롤러로의 전환을 시작할 것을 권장합니다.
👉 [자세히 보기](https://kubernetes.io/blog/2025/11/11/ingress-nginx-retirement/)

## 🔹 Spring Boot - Spring Security 2025-11 Releases - 7.0.0, 6.5.7, 6.4.13 available now!
Spring Security 팀과 기여자들을 대표하여 버전 7.0.0, 6.5.7, 6.4.13의 출시를 발표하게 되어 기쁩니다. 7.0.0의 주요 업데이트 내용은 관련 문서의 "What's New" 섹션에서 확인할 수 있으며, 전체 변경 사항은 각 버전의 변경 로그를 참고하시기 바랍니다. 추가적으로 프로젝트 페이지, GitHub, 이슈, 문서 링크도 제공됩니다.
👉 [자세히 보기](https://spring.io/blog/2025/11/17/spring-security-releases)

## 🔹 Docker - Making the Most of Your Docker Hardened Images Trial – Part 1
이 기술 블로그 글은 Docker Hardened Images의 첫 번째 사용 단계에 대해 설명합니다. 이 이미지들은 보안을 염두에 두고 설계된 최소한의 베이스 이미지를 제공하며, 불필요한 패키지를 제거하고 사전에 패치를 적용하여 지속적으로 유지 관리됩니다. 이러한 이미지를 사용하면 애플리케이션의 보안 기반을 강화할 수 있으며, 취약점을 포함한 기반에서 벗어나 보다 안전한 프로덕션 환경을 구축할 수 있습니다.
👉 [자세히 보기](https://www.docker.com/blog/making-the-most-of-your-docker-hardened-images-trial-part-1/)

## 🔹 Java - JEP targeted to JDK 26: 524: PEM Encodings of Cryptographic Objects (Second Preview)
블로그 글 요약: JDK 26을 목표로 한 JEP 524는 암호 객체의 PEM 인코딩에 관한 두 번째 프리뷰입니다. 이 JEP는 암호화 객체를 PEM 형식으로 인코딩하는 기능을 제공합니다. 더 자세한 내용은 해당 링크에서 확인할 수 있습니다.
👉 [자세히 보기](https://inside.java/2025/11/17/jep524-target-jdk26/)

## 🔹 Golang - Go’s Sweet 16
제목: Go의 16번째 생일

요약: Go 프로그래밍 언어의 16번째 생일을 축하하는 글입니다. 이 블로그 글에서는 Go의 개발 역사와 성과를 되짚어보고, Go 커뮤니티의 성장과 발전을 기념하고 있습니다. Go 언어는 지난 16년 동안 많은 사랑을 받으며, 개발자들 사이에서 중요한 도구로 자리 잡았습니다.
👉 [자세히 보기](https://go.dev/blog/16years)

