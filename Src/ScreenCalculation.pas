unit ScreenCalculation;

{$MODE OBJFPC}
{$LONGSTRINGS ON}
{$ASSERTIONS ON}
{$RANGECHECKS ON}
{$BOOLEVAL OFF}

interface

type
  TInputData = record
    Width: Double;
    Length: Double;
    Gap: Double;
  end;

  TManualScreen = record
    ExternalWidth: Double;
    Length: Double;
    Weight: Double;
    ProfileNumber: Integer;
    ProfileLength: Double;
  end;

const
  MinWidth = 0.3;
  MaxWidth = 1.5;
  MinLength = 0.5;
  MaxLength = 2.65;

procedure CalcManualScreen(out Scr: TManualScreen; const InputData: TInputData);

implementation

uses
  Math, Measurements;

const
  ProfileWidth = 0.0095;  // Ширина профиля 3999

function CalcProfileNumber(const Width, Gap: Double): Integer;
begin
  Result := Ceil((Width - Gap) / (ProfileWidth + Gap));
  Assert(Result > 0);
end;

function CalcProfileWeight(const Length: Double): Double;
begin
  Result := 1 * Length - 0.001;
  Assert(Result > 0);
end;

function CalcGridWeight(const Length: Double; const ProfileNumber: Integer): Double;
begin
  Result := CalcProfileWeight(Length) * ProfileNumber;
  Assert(Result > 0);
end;

function CalcBottomBalkWeight(const Length: Double): Double;
begin
  Result := 3 * Length - 0.006;
  Assert(Result > 0);
end;

function CalcIntermediateRakerWeight(const Length: Double): Double;
begin
  Result := 1 * Length - 0.022;
  Assert(Result > 0);
end;

function CalcTopSlideWeight(const Width, Length: Double): Double;
begin
  Result := 32.58 * Length * Width + 1.79 * Length + 4.11 * Width;
  Assert(Result > 0);
end;

function CalcTopPropWeight(const Length: Double): Double;
begin
  Result := 4 * Length - 0.01;
  Assert(Result > 0);
end;

function CalcProfileLength(const ScreenLength: Double): Double;
begin
  Result := ScreenLength - Mm(356);
  Assert(Result > 0);
end;

function CalcScreenWeight(const ExternalWidth, ProfileLength, InternalWidth: Double;
  const ProfileNumber: Integer): Double;
const
  OtherWeight = 1.7;
begin
  Result := CalcBottomBalkWeight(ExternalWidth) +
    CalcIntermediateRakerWeight(ExternalWidth) +
    CalcTopSlideWeight(InternalWidth, Mm(340)) +
    CalcTopPropWeight(ExternalWidth + Mm(200)) +
    CalcGridWeight(ProfileLength, ProfileNumber) + OtherWeight;
end;

function CalcInternalWidth(const ExternalWidth: Double): Double;
begin
  Result := ExternalWidth - Mm(15);
  Assert(Result > 0);
end;

procedure CalcManualScreen(out Scr: TManualScreen; const InputData: TInputData);
var
  InternalWidth: Double;
begin
  Scr.ExternalWidth := InputData.Width;
  Scr.Length := InputData.Length;

  InternalWidth := CalcInternalWidth(Scr.ExternalWidth);
  Scr.ProfileNumber := CalcProfileNumber(InternalWidth, InputData.Gap);
  Scr.ProfileLength := CalcProfileLength(Scr.Length);
  Scr.Weight := CalcScreenWeight(Scr.ExternalWidth, Scr.ProfileLength,
    InternalWidth, Scr.ProfileNumber);
end;

end.
