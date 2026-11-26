"""Kiem ke output cac notebook va dong bo ho so nop do an DS317.

Script nay quet toan bo 9 thu muc con trong 05_Output_Cac_Notebook/,
thong ke so luong file thuc te (bo qua .gitkeep) va ho tro sao chep
cac tep trong so / ket qua nhe sang DS317_R11_Nhom03_HoSoNopDoAn/.
"""

import argparse
from pathlib import Path
import shutil
import sys


MAX_SYNC_BYTES = 95 * 1024 * 1024

RUNNER_DIRS = (
    "07_Runner_Song_Song_1_Baseline_M1_M2_M3",
    "08_Runner_Song_Song_2_M4_M5_M6_M7",
)

RESULT_EXTENSIONS = {".csv", ".json", ".md", ".png", ".txt"}


def inventory_outputs(output_root: Path) -> list[tuple[str, int, int]]:
    """Thong ke so luong file va tong dung luong theo tung thu muc.

    Args:
        output_root (Path): Duong dan thu muc 05_Output_Cac_Notebook.

    Returns:
        list[tuple[str, int, int]]: Danh sach gom (ten thu muc,
            so file khong tinh .gitkeep, tong kich thuoc theo byte).
    """
    rows: list[tuple[str, int, int]] = []
    for subdir in sorted(output_root.iterdir()):
        if not subdir.is_dir():
            continue
        files = [
            path
            for path in subdir.rglob("*")
            if path.is_file() and path.name != ".gitkeep"
        ]
        total_bytes = sum(path.stat().st_size for path in files)
        rows.append((subdir.name, len(files), total_bytes))
    return rows


def _collect_dir_files(
    src_dir: Path,
    dst_dir: Path,
    max_bytes: int,
    allowed_exts: set[str] | None,
    sync_pairs: list[tuple[Path, Path]],
    skipped_large: list[tuple[Path, int]],
) -> None:
    """Thu thap file hop le tu mot thu muc nguon sang thu muc dich.

    Args:
        src_dir (Path): Thu muc nguon can quet de quy.
        dst_dir (Path): Thu muc dich tuong ung.
        max_bytes (int): Nguong dung luong toi da cho phep (byte).
        allowed_exts (set[str] | None): Tap duoi file cho phep hoac
            None neu lay tat ca file.
        sync_pairs (list[tuple[Path, Path]]): Danh sach cap nguon-dich.
        skipped_large (list[tuple[Path, int]]): Danh sach file qua lon.
    """
    if not src_dir.exists():
        return
    for src in sorted(src_dir.rglob("*")):
        if not src.is_file() or src.name == ".gitkeep":
            continue
        if allowed_exts is not None:
            if src.suffix.lower() not in allowed_exts:
                continue
        size = src.stat().st_size
        if size > max_bytes:
            skipped_large.append((src, size))
            continue
        rel = src.relative_to(src_dir)
        sync_pairs.append((src, dst_dir / rel))


def collect_sync_pairs(
    output_root: Path,
    submission_root: Path,
    max_bytes: int,
) -> tuple[list[tuple[Path, Path]], list[tuple[Path, int]]]:
    """Thu thap danh sach cap nguon-dich can dong bo va file qua lon.

    Args:
        output_root (Path): Duong dan 05_Output_Cac_Notebook.
        submission_root (Path): Duong dan DS317_R11_Nhom03_HoSoNopDoAn.
        max_bytes (int): Nguong dung luong toi da cho phep copy (byte).

    Returns:
        tuple[list[tuple[Path, Path]], list[tuple[Path, int]]]:
            Cap (danh sach (nguon, dich), danh sach file vuot nguong).
    """
    sync_pairs: list[tuple[Path, Path]] = []
    skipped_large: list[tuple[Path, int]] = []

    model_dest = submission_root / "05_Model"
    result_dest = submission_root / "06_Results"

    for runner_name in RUNNER_DIRS:
        runner_dir = output_root / runner_name
        _collect_dir_files(
            src_dir=runner_dir / "saved_models",
            dst_dir=model_dest / runner_name,
            max_bytes=max_bytes,
            allowed_exts=None,
            sync_pairs=sync_pairs,
            skipped_large=skipped_large,
        )
        _collect_dir_files(
            src_dir=runner_dir / "results",
            dst_dir=result_dest / "Runner_v2",
            max_bytes=max_bytes,
            allowed_exts=RESULT_EXTENSIONS,
            sync_pairs=sync_pairs,
            skipped_large=skipped_large,
        )

    extra_sources = (
        ("02_DS317_02_Kham_Pha_DAMA_26_Dac_Trung", "DAMA_26_Dac_Trung"),
        ("06_DS317_Tong_Hop_Xuat_So_Lieu_BTVN", "BTVN_TongHop"),
    )
    for src_name, dst_name in extra_sources:
        _collect_dir_files(
            src_dir=output_root / src_name,
            dst_dir=result_dest / dst_name,
            max_bytes=max_bytes,
            allowed_exts=RESULT_EXTENSIONS,
            sync_pairs=sync_pairs,
            skipped_large=skipped_large,
        )

    return sync_pairs, skipped_large


def format_mb(num_bytes: int) -> str:
    """Dinh dang dung luong byte sang chuoi MB.

    Args:
        num_bytes (int): So byte can dinh dang.

    Returns:
        str: Chuoi dung luong theo don vi MB.
    """
    return f"{num_bytes / (1024 * 1024):.2f} MB"


def run_sync(
    output_root: Path,
    submission_root: Path,
    dry_run: bool,
    max_bytes: int,
) -> int:
    """Thuc thi kiem ke va dong bo file tu 05_Output_Cac_Notebook.

    Args:
        output_root (Path): Duong dan 05_Output_Cac_Notebook.
        submission_root (Path): Duong dan DS317_R11_Nhom03_HoSoNopDoAn.
        dry_run (bool): Neu True chi thong ke va in ke hoach dong bo.
        max_bytes (int): Nguong kich thuoc file toi da duoc copy.

    Returns:
        int: Ma thoat (0 neu thanh cong).
    """
    if not output_root.exists():
        print(f"[ERROR] Khong tim thay thu muc: {output_root}")
        return 1

    rows = inventory_outputs(output_root)
    print("=== KIEM KE 05_Output_Cac_Notebook ===")
    total_files = 0
    total_bytes = 0
    for name, count, size in rows:
        total_files += count
        total_bytes += size
        print(f"  - {name}: {count} file(s), {format_mb(size)}")
    print(f"  TONG CONG: {total_files} file(s), {format_mb(total_bytes)}")

    sync_pairs, skipped_large = collect_sync_pairs(
        output_root=output_root,
        submission_root=submission_root,
        max_bytes=max_bytes,
    )

    mode_label = "DRY-RUN" if dry_run else "THUC THI"
    print(f"\n=== KE HOACH DONG BO ({mode_label}) ===")
    print(f"  - So file du dieu kien dong bo: {len(sync_pairs)}")
    print(
        f"  - So file bo qua (> {format_mb(max_bytes)}): "
        f"{len(skipped_large)}"
    )

    for path, size in skipped_large:
        rel = path.relative_to(output_root)
        print(f"    [SKIP-LARGE] {rel} ({format_mb(size)})")

    if dry_run:
        return 0

    copied = 0
    for src, dst in sync_pairs:
        dst.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(src, dst)
        copied += 1

    print(f"  - Da dong bo {copied} file(s) sang {submission_root}")
    return 0


def parse_args(argv: list[str]) -> argparse.Namespace:
    """Phan tich tham so dong lenh.

    Args:
        argv (list[str]): Danh sach doi so truyen vao tu dong lenh.

    Returns:
        argparse.Namespace: Doi tuong chua cac tham so da phan tich.
    """
    default_output = Path(__file__).resolve().parent
    default_repo = default_output.parent
    default_submission = default_repo / "DS317_R11_Nhom03_HoSoNopDoAn"

    parser = argparse.ArgumentParser(
        description=(
            "Kiem ke 05_Output_Cac_Notebook va dong bo sang "
            "DS317_R11_Nhom03_HoSoNopDoAn."
        )
    )
    parser.add_argument(
        "--output-root",
        type=Path,
        default=default_output,
        help="Thu muc chua output cac notebook.",
    )
    parser.add_argument(
        "--submission-root",
        type=Path,
        default=default_submission,
        help="Thu muc ho so nop do an dich.",
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Chi kiem ke va xem truoc, khong ghi file.",
    )
    parser.add_argument(
        "--max-mb",
        type=float,
        default=95.0,
        help="Gioi han kich thuoc toi da (MB) cho moi file dong bo.",
    )
    return parser.parse_args(argv)


def main() -> int:
    """Diem vao chinh cua script kiem ke va dong bo.

    Returns:
        int: Ma thoat cua chuong trinh.
    """
    args = parse_args(sys.argv[1:])
    max_bytes = int(args.max_mb * 1024 * 1024)
    return run_sync(
        output_root=args.output_root,
        submission_root=args.submission_root,
        dry_run=args.dry_run,
        max_bytes=max_bytes,
    )


if __name__ == "__main__":
    raise SystemExit(main())
